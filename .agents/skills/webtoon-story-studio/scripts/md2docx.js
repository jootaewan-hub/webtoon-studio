const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, LevelFormat, AlignmentType, PageOrientation, Footer, PageNumber } = require('docx');

const [,, inPath, outPath, orient] = process.argv;
const md = fs.readFileSync(inPath, 'utf8').split('\n');
const landscape = orient === 'landscape';
const FONT = 'Malgun Gothic';
const PAGE_W = landscape ? 16838 : 11906, MARGIN = 1134;
const CONTENT_W = PAGE_W - MARGIN * 2;

function runs(text, base = {}) {
  const out = []; const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g; let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out.length ? out : [new TextRun({ text: '', ...base })];
}

const border = { style: BorderStyle.SINGLE, size: 4, color: '9AA1AC' };
const borders = { top: border, bottom: border, left: border, right: border };

function table(rows) {
  const header = rows[0], body = rows.slice(1);
  const n = header.length;
  // column weights: short first columns, wide text columns
  let weights;
  if (n === 4) weights = [9, 10, 46, 35];
  else if (n === 5 && header[0] === '컷') weights = [7, 8, 17, 40, 28];
  else if (n === 10 && header[0] === '샷') weights = [6, 6, 7, 11, 17, 11, 10, 10, 14, 8];
  else if (n === 6 && header[0] === '게이트') weights = [8, 14, 22, 30, 8, 12];
  else if (n === 5) weights = [10, 16, 26, 22, 26];
  else if (n === 3) weights = [40, 25, 35];
  else weights = Array(n).fill(1);
  const sum = weights.reduce((a, b) => a + b, 0);
  const widths = weights.map(w => Math.floor(CONTENT_W * w / sum));
  widths[n - 1] += CONTENT_W - widths.reduce((a, b) => a + b, 0);
  const cell = (txt, i, head) => new TableCell({
    borders, width: { size: widths[i], type: WidthType.DXA },
    shading: head ? { fill: 'E4E8EE', type: ShadingType.CLEAR, color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: txt.split(' / ').map(part => new Paragraph({ spacing: { after: 40 }, children: runs(part, { size: 18, bold: head || undefined }) })),
  });
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: header.map((h, i) => cell(h, i, true)) }),
           ...body.map(r => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, i, false)) }))],
  });
}

const children = [];
for (let i = 0; i < md.length; i++) {
  const line = md[i];
  if (!line.trim()) continue;
  if (line.startsWith('|')) {
    const rows = [];
    while (i < md.length && md[i].startsWith('|')) {
      const cells = md[i].trim().replace(/^\||\|$/g, '').split('|').map(s => s.trim());
      if (!cells.every(c => /^-+$/.test(c))) rows.push(cells);
      i++;
    }
    i--;
    children.push(table(rows));
    children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
    continue;
  }
  let m;
  if ((m = line.match(/^(#{1,4}) (.*)$/))) {
    const lvl = [HeadingLevel.TITLE, HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3][m[1].length - 1];
    children.push(new Paragraph({ heading: lvl, children: runs(m[2]) }));
    continue;
  }
  if ((m = line.match(/^(\s*)- (.*)$/))) {
    children.push(new Paragraph({ numbering: { reference: 'bul', level: m[1].length >= 2 ? 1 : 0 }, spacing: { after: 60 }, children: runs(m[2]) }));
    continue;
  }
  const centered = /^\*— 끝 —\*$/.test(line.trim());
  children.push(new Paragraph({ alignment: centered ? AlignmentType.CENTER : undefined, spacing: { after: 160, line: 360 }, children: runs(line) }));
}

const doc = new Document({
  styles: {
    default: { document: { run: { font: { ascii: FONT, eastAsia: FONT, hAnsi: FONT }, size: 21 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { size: 40, bold: true, font: { ascii: FONT, eastAsia: FONT, hAnsi: FONT } }, paragraph: { spacing: { after: 360 }, alignment: AlignmentType.CENTER } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 30, bold: true }, paragraph: { spacing: { before: 480, after: 200 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 25, bold: true }, paragraph: { spacing: { before: 320, after: 160 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 21, bold: true, color: '3A4456' }, paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: 'bul', levels: [
    { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } },
    { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1080, hanging: 270 } } } },
  ] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838, orientation: landscape ? PageOrientation.LANDSCAPE : PageOrientation.PORTRAIT }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '777777' })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(outPath, b); console.log('wrote', outPath); });
