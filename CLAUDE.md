# CLAUDE.md — webtoon-studio

이 저장소는 웹툰 원작 기획·집필·콘티 작업장이다. 작업을 시작하기 전에 `CONTINUE.md`를 읽는다.

- 언어: 한국어. 근거를 밝히고, 미확인·추측은 표시한다.
- 진행 방식: `skills/webtoon-story-studio`의 결정 게이트(G0~G12)를 따른다. 결정은 `five-doors/decisions.md`에 한 줄씩 남긴다.
- 그림은 그리지 않는다. 작화는 ChatGPT와 Codex가 맡는다. Claude는 사양, 프롬프트, 콘티를 만든다.
- 기준 우선순위: `decisions.md` > `story/bible.md` 0-2 확정 외형 > LOCK 문단(`handoff/`) > `story/novel.md`·`script.md`.
- **작업 순서(2026-10-08 사용자 지시)**: 인물 설정(G2 심화 바이블 + 외형 LOCK)을 끝까지 확정한 뒤에 소설(G4)을 쓴다. 소설을 쓴 뒤에는 외형 단어를 바이블과 대조한다.
- 이미지 생성기의 이용 정책을 피해 가는 프롬프트는 만들지 않는다. 노출 컷은 도구 경로 B(성인 허용 도구·사람 작가)나 가림 장치판으로 처리한다(`skills/webtoon-story-studio/references/image_tools.md`).
- 분량이 큰 작업(회차별 콘티 등)은 서브에이전트에 병렬로 맡기고, 별도 에이전트로 검수한다.
- 도구:
  - `python3 five-doors/tools/studio.py <명령> --dir five-doors` (docx, pack 등)
  - 킷은 `skills/webtoon-adaptation-kit/scripts/kit.py`(v2), 스튜디오 → 킷 입력은 `from_studio.py`
  - 콘티 검사 `tools/check_board.py`, 효과음 `tools/sfx_tools.py`, 연출 노트 2부 `tools/direction_scenes.py`, 애니 `tools/anim_tools.py`, 인계 `tools/build_handoff.py`
  - docx 변환에는 `npm i -g docx`가 필요하다.
