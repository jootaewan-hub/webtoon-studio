# source 폴더 — 원본

| 파일 | 내용 |
|---|---|
| novel.md / novel.docx | 소설 원본 |
| storyboard.md / storyboard.docx | 웹툰 콘티 (제작 개요·캐릭터 시트·스타일·장별 콘티 표) |

- `.md`는 kit.py가 읽는 원본입니다. 고친 뒤 `python kit.py import`를 실행하면 data/와 outputs/가 갱신됩니다.
- `.docx`는 읽기·인쇄·공유용입니다. `.md`를 고친 뒤 `python kit.py docx`로 다시 만듭니다. Word에서 고친 내용은 자동 반영되지 않습니다.
