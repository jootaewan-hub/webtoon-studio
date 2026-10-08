# CLAUDE.md — webtoon-studio

이 저장소는 웹툰 원작 기획·집필·콘티 작업장이다. 작업을 시작하기 전에 `CONTINUE.md`를 읽는다.

- 언어: 한국어. 근거를 밝히고, 미확인·추측은 표시한다.
- 진행 방식: `skills/webtoon-story-studio`의 결정 게이트(G0~G12)를 따른다. 결정은 `five-doors/decisions.md`에 한 줄씩 남긴다.
- 그림은 그리지 않는다. 작화는 ChatGPT와 Codex가 맡는다. Claude는 사양, 프롬프트, 콘티를 만든다.
- 기준 우선순위: `decisions.md` > `story/bible.md` 0-2 확정 외형 > LOCK 문단(`handoff/`) > `story/novel.md`·`script.md`.
- 분량이 큰 작업(회차별 콘티 등)은 서브에이전트에 병렬로 맡기고, 별도 에이전트로 검수한다.
- 도구:
  - `python3 five-doors/tools/studio.py <명령> --dir five-doors` (docx, pack 등)
  - 킷은 `skills/webtoon-adaptation-kit/scripts/kit.py`
  - docx 변환에는 `npm i -g docx`가 필요하다.
- 스킬 원본은 `skills/<이름>/` 하나다. 고친 뒤에는 `python3 tools/sync_skills.py`로 `.claude/skills/` 사본과 `skills/*.skill` 패키지를 맞춘다(`--check`는 점검만).
