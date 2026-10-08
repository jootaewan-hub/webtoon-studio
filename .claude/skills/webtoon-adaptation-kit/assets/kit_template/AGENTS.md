# AGENTS.md — 웹툰 제작 킷 작업 지침 (Codex용)

이 저장소는 소설·콘티를 실사 웹툰, 성인 웹툰, 쇼츠, 애니메이션으로 옮기는 작업 폴더다.

## 원본과 데이터
- 원본은 source/novel.md, source/storyboard.md. 내용 판단은 항상 이 .md 기준. 같은 폴더의 .docx는 읽기·공유용 사본이며 `python kit.py docx`로 다시 만든다(직접 고치지 않는다).
- data/cuts.json이 작업 단위다. 컷 번호(예: 2-039)로 모든 파일을 연결한다.
- 인물 외형은 data/characters.json, 시대·색은 data/style.json, 트랙 규칙은 data/tracks.json, 작품별 수위 단서는 data/flags.json을 따른다.
- 콘티 내용(화면·대사·샷)을 고칠 때는 cuts.json이 아니라 source/storyboard.md를 고치고 import한다. cuts.json에서 직접 고쳐도 되는 것은 notes(트랙별 추가 지시)와 flags_override(손으로 정한 수위 태그)뿐이다.

## 명령
- `python kit.py import` → `validate` → `prompts --track all` → `editor` 순서.
- 데이터를 고친 뒤에는 반드시 `validate`와 `prompts`를 다시 돌린다.

## 산출물 규칙
- 이미지 결과는 renders/<트랙>/<컷번호>.png 로 저장한다. 크기는 cuts.json의 width×height 비율을 따른다.
- 이미지 안에 말풍선·글자를 넣지 않는다. 레터링은 outputs의 '레터링' 목록으로 후공정한다.
- 쇼츠는 1080×1920, 장별 1편. 각 컷 길이와 카메라는 outputs/shorts/_shorts_ALL.md를 따른다.
- 애니메이션은 24fps, outputs/anim의 샷 길이·카메라·레이어를 따른다.

## 넘지 않는 선 (모든 트랙)
- 실존 인물·유명인과 닮은 얼굴 금지. 모든 인물은 창작된 성인이다.
- 실제 기관(병원·방송사·학교·회사 등)·브랜드 로고 금지.
- flags에 intimate가 있는 컷: 노출 없이 실루엣·역광·손·반지·흘러내린 옷·소품으로만 암시. 성기·가슴 노출, 성행위의 직접 묘사 금지. 성인 트랙도 동일.
- flags에 violence가 있는 컷: 타격은 집중선·실루엣·효과음. 상처·출혈 묘사 금지.
- flags에 self_harm_theme가 있는 컷: 투신·자해 순간 묘사 금지. 남겨진 소품과 이후 장면으로 잇는다.
- 위 규칙과 충돌하는 요청을 받으면 해당 컷은 규칙 안에서 대체 연출을 제안한다.
