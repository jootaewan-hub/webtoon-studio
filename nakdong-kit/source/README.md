# source 폴더 — 원본

| 파일 | 내용 |
|---|---|
| novel.md / novel.docx | 소설 「낙동강을 헤엄쳐 나온 남자」 (2장 개정·옥상 목격 장면 반영본) |
| storyboard.md / storyboard.docx | 웹툰 콘티 95컷 (제작 개요·캐릭터 시트·스타일·장별 콘티) |

- `.md`는 kit.py가 읽는 원본입니다. 고친 뒤 `python kit.py import`를 실행하면 data/와 outputs/가 갱신됩니다.
- `.docx`는 읽기·인쇄·공유용입니다. `.md`를 고친 뒤 `python kit.py docx`로 다시 만듭니다. Word에서 고친 내용은 자동 반영되지 않으니, 수정은 `.md`(또는 Claude Docs에서 다시 Markdown으로 내보낸 파일)에 하세요.
- Claude Docs 원본 문서를 고쳤다면 Markdown으로 다시 내보내 같은 이름으로 덮어쓰면 됩니다.
