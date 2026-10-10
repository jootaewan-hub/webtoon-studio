# 「깡통 바이올린」 웹툰 콘티 킷 (G9)

`webtoon-adaptation-kit` 템플릿으로 만든 작업 폴더다. 작품 설정에 맞게 바꿨다. 아동 주인공 작품이라 성인 트랙이 없고, 아동 보호·12세 이상 규칙이 모든 컷 금지 목록에 붙는다(`data/tracks.json`).

| 결과물 | 위치 |
|---|---|
| 콘티 원본 | `source/storyboard.md`(.docx), 규격 `SPEC.md`, 밀도 표본 `samples/density_S1.md` |
| 컷 이미지 프롬프트(정본) | `out/cel/_cel_ALL_ep1~3.md`, 컷별 `out/cel/<컷>.md`, `out/cel/cel_prompts.jsonl` |
| 컷 영어 사양(프롬프트 재료) | `source/cut_spec_ep1~3.jsonl` |
| 씬 색인(작가용) | `source/scene_index.md` |
| 썸네일·보드·편집기 | `thumbs/*.svg`, `tools/board.html`, `tools/editor_ready.html` |
| 쇼츠·애니 참고 | `outputs/shorts/`, `outputs/anim/` |
| 작가 메모 | `source/work_notes.md` |

## 다시 만들기 (상위 폴더 `landfill-orchestra/`에서)

```
python3 tools/scene_index.py                      # 디자인을 고쳤으면 씬 색인 갱신
cd storyboard && python3 kit.py import --replace && python3 kit.py validate && python3 kit.py thumbs-auto \
  && python3 kit.py prompts --track all && python3 kit.py board && python3 kit.py editor && python3 kit.py docx && cd ..
python3 tools/cut_prompts.py build                # 컷 이미지 프롬프트(정본)
```

작가 조각(검수 전 원본)은 `parts_v1_before_review/`에 보관만 한다. 합본 뒤에는 `source/storyboard.md`가 원본이다(검수 반영본). `tools/sb_merge.py`는 `parts/`가 없으면 멈추므로 합본을 덮어쓰지 않는다. 고칠 때는 이 파일과 `source/cut_spec_ep*.jsonl`을 함께 고친다.

점검: `python3 tools/sb_check.py storyboard/source/storyboard.md --ep 1 --scenes 1-34 --spec storyboard/source/cut_spec_ep1.jsonl`(화별). 합본 점검은 `python3 tools/cut_prompts.py check`.
