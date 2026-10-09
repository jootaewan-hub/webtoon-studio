# 의상 고증 보고서 — 깡통 바이올린 (작성 2026-10-09)

검증 대상: `design/characters.json`(outfits·face), `design/outfits_en.json`(55문장), `design/style_guide.md` 6절·7-1절, `design/outfit_schedule.json`, `design/scene_presets.json`(씬별 실제 배정).
이 문서는 파일을 고치지 않는다. 바꿀 내용은 표 2 수정안으로만 낸다. `decisions.md` 기준으로 계절·본선 날·2003 의상은 '잠정'(G7, Claude 제안)이므로 고쳐도 된다. 다만 섬 아이 디자인(머리 하나+옷 색 하나)과 본선 규칙(제일 좋은 옷+빨간 손수건)은 '확정'이다. 이것을 건드리는 권고에는 **[확정 변경, 사용자 승인 필요]**를 붙였다.

판정 기준
- **맞음**: 그 시대에 그 물건이나 차림이 있었다는 것을 직접 뒷받침하는 출처가 있을 때만 쓴다.
- **미확인**: 그럴듯하지만 직접 출처를 찾지 못했을 때 쓴다. 계절이 맞는지는 괄호에 따로 적었다.
- **수정 권장**: 출처나 대본과 어긋나거나, 영어 문장이 시대 착오 그림을 부를 위험이 클 때 쓴다.
- **추측**: 해석이라는 표시다. '(검색 요약)'은 검색 결과 요약에만 나오고 본문을 직접 열어 보지 못한 근거라서 약한 근거다.
- 저작권: 페이지 문장은 요약만 했다. 사진은 링크만 달았다.

## 출처 목록

| 키 | 출처 | 확인한 내용(요약) |
|---|---|---|
| S1 | [한국민족문화대백과 '군복'](https://encykorea.aks.ac.kr/Article/E0006624) | 1985년에 계획을 시작해 1991-11-23부터 전투복·전투모·야전상의를 수풀지대용 얼룩무늬로 착용. 그 전(1987~88) 야전상의는 얼룩무늬가 아님. 기본색은 이 항목에 없음 |
| S2 | [한국민족문화대백과 '몸뻬'](https://encykorea.aks.ac.kr/Article/E0079810) | 일제 말 전시복에서 왔음. 바짓가랑이가 넓고 부리를 오므림. 나중에는 고무줄 허리에 인조견·합성섬유. 광복 뒤 한국전쟁과 산업화를 거치며 도시·농촌의 노동복·일상복으로 자리 잡음. 이칭 '일바지' |
| S3 | [한국민족문화대백과 '넝마주이'](https://encykorea.aks.ac.kr/Article/E0068876) | 망태기와 집게로 폐품을 모아 팖. 1962년 근로재건대, 1981년 서울시 강제 이주, 1986년 넝마공동체 |
| S4 | [한국민족문화대백과 '교복'](https://encykorea.aks.ac.kr/Article/E0005480) | 1983년 지정 금지, 1986년 2학기 재허용. 새 교복은 학교마다 개성 있고 밝은 색의 다양한 형태. 1990년대 교복은 대부분 블레이저형 |
| S5 | [국가기록원 '교복'](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do) | 1986년부터 학교장 재량, 1993년 약 83% 학교가 교복. 대부분 남학생은 상의+바지 정장, 여학생은 상의+스커트 정장. 1982년 두발 자유화 |
| S6 | [한국민족문화대백과 '머리 모양'](https://encykorea.aks.ac.kr/Article/E0018097) | 1980년대 여성: 이층 보브. 중반에는 스트레이트 파마와 풀어 헤친 듯한 웨이브 파마, 무스·젤·스프레이로 앞머리를 세움. 1960년대 바가지머리(1967, 여성) |
| S7 | [경향신문 2023 '옛날잡지'(레이디경향 1989 신년호 인용)](https://www.khan.co.kr/article/202302281813001) | 1980년대 할머니들은 여전히 쪽을 찌고 한복을 일상복으로 입음 |
| S8 | [경향신문 2000 '잃어버린 시절을 찾아서—미장원'](https://www.khan.co.kr/article/200011231651001) | 중년 여성은 고데 웨이브나 로트로 세게 만 오래가는 파마(우찌마끼·소도마끼) |
| S9 | [서울신문 2004-03-17 트레이닝복 기사](https://www.seoul.co.kr/news/life/2004/03/17/20040317024004) | 1980년대 동네 운동복: 노란 상하의에 검은 옆선, 남색 바탕에 빨간 줄 한 줄(왼가슴 태권 문양). 2003~04 유행: 벨로어·새틴, 밝은 색, 섞어 입기 |
| S10 | [경향신문 2003-07-10 '츄리닝'](https://www.khan.co.kr/article/200307101630251) | 1970년대 말 이소룡풍: 몸에 붙는 러닝셔츠에 헐렁한 노란 츄리닝. 1970년대 중반 아디다스 바지 옆 세 줄. 2003년: 날렵한 핏, 옆선 있는 9~10부 바지 |
| S11 | [한국일보 2003-12-19 패션 10대 뉴스](https://www.hankookilbo.com/news/article/200312190021393066) | (검색 요약) 2003년 트레이닝복의 고급 패션화가 그해 첫째 뉴스 |
| S12 | [한국민족문화대백과 '양복'](https://encykorea.aks.ac.kr/Article/E0035532) | 1970년대 초반 넓은 깃·피크 라펠, 판탈롱 영향으로 넓은 바지 부리. 1978년부터 깃·넥타이 폭이 좁아짐. 1988년부터 블루종형 가죽 점퍼 유행 |
| S13 | [국가기록원 '간소복'](https://theme.archives.go.kr/next/koreaOfRecord/simpleClothes.do) | 공무원 간소복이 1970년대 새마을복으로 바뀌었다가 1996년 자율화 분위기 속에 사라짐. 1980년대 실태는 서술 없음 |
| S14 | [서울신문 2022-08-15 민방위복](https://m.seoul.co.kr/news/life/2022/08/15/20220815500016) | 노란 민방위복은 2005년(민방위대 창설 30주년)부터. 1987~88년 색은 이 기사에 없음 |
| S15 | [국가기록원 '한복에서 양복으로'](https://theme.archives.go.kr/next/education2010/wear01.do) | 1970년대 양복이 평상복이 되고, 한복은 큰일 있는 외출·명절 옷. 1980년대 초 기성복 확산 |
| S16 | [경향신문 2016 '응답하라 1988 브랜드'](https://www.khan.co.kr/article/201601081200221) | 1988 무렵 공갈 목폴라(여러 색), 국산 운동화 등 |
| S17 | [한국민족문화대백과 '고무신'](https://encykorea.aks.ac.kr/Article/E0003567) | 1960년경부터 운동화가 대중화되면서 고무신 선호가 떨어짐 |
| S18 | [오마이뉴스 2011 메리야스 회고](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0001611657) | 어릴 적 속옷은 흰 백양 러닝셔츠(개인 회고, 연대 미상) |
| S19 | [Wikipedia 'Seoul' 기후표(1991–2020 평년값)](https://en.wikipedia.org/wiki/Seoul) | 평균/최고/최저(°C): 1월 −2.0/2.1/−5.5, 4월 12.6/17.9/8.0, 5월 18.2/23.6/13.5, 6월 22.7/27.6/18.7, 7월 25.3/29.0/22.3, 9월 21.7/26.2/17.7, 10월 15.0/20.2/10.6, 11월 7.5/11.9/3.5. 1987~88년 실제 기온 아님(평년값) |
| S20 | [경향신문 2010 '100년을 엿보다—이발소'](https://www.khan.co.kr/article/201006271815342) | 1960~70년대 아이들이 이발소에서 상고머리·빡빡머리 등으로 깎음. 1980년 전후 이발소 쇠락 |
| S21 | [숙명여대 논문 초록(S여대 졸업앨범 1982~2016)](https://scholarworks.sookmyung.ac.kr/handle/2020.sw.sookmyung/9017) | 1984·1986년에는 블라우스+스커트의 로맨틱·페미닌 이미지 선호. 전 기간 허리 길이 재킷+무릎 길이 타이트스커트가 많음 |
| S22 | [A] 『난지도 그 향기를 되찾다』(서울시, 2006), [PDF](https://www.seoulsolution.kr/sites/default/files/policy/%EB%82%9C%EC%A7%80%EB%8F%84%EA%B7%B8%ED%96%A5%EA%B8%B0%EB%A5%BC.pdf) | research/notes.md 기존 관찰: 하역장의 사람들이 어둡고 두꺼운 옷, 머릿수건, 등에 진 대바구니, 빨강·파랑 웃옷이 드문드문(사진 연도 미상) |
| S23 | [국가기록원 교복 wear05](https://theme.archives.go.kr/next/education2010/wear05.do) | (research/notes 기존 확인) 국민학교는 자유복, 일부 사립만 교복 |
| S24 | [경향신문 2017 '금지를 금지하라(13)'](https://www.khan.co.kr/article/201708132131005) | 자율화 전 교복은 남학생 육군복, 여학생 세라복(해군복)을 본뜸. 재건복은 사파리 재킷 |
| S25 | [한국일보 2003-01-10 복고풍 캐주얼](https://www.hankookilbo.com/news/article/200301100084193889) | 2003년 '세미복고': 큰 로고·문양 청바지, 굵은 벨트, 큰 로고 셔츠 |
| S26 | [국가기록원 '판자촌'](https://theme.archives.go.kr/next/koreaOfRecord/panjaChon.do) | (research/notes 기존 확인) 1950년대 판잣집 재료: 합판·깡통·생철·천막천 |
| S27 | [한국민족문화대백과 '비녀'](https://encykorea.aks.ac.kr/Article/E0025100) | (검색 요약) 쪽진머리가 풀리지 않게 비녀를 씀 |
| S28 | [경향신문 2012 쇼단 단장 회고](https://www.khan.co.kr/article/201208241932115) | 1970년대 쇼단 전성기 회고. 복장 서술은 없음(검색 요약) |

사진으로 직접 대조할 곳(링크만): [서울역사아카이브 1984~1988](https://museum.seoul.go.kr/archive/archiveNew/NR_archiveList.do?ctgryId=CTGRY772&type=B), [서울기록원 서울사진아카이브](https://archives.seoul.go.kr/contents/seoul-photo-archive), [국가기록원 운동회 사진](https://theme.archives.go.kr/next/photo/sport_day01List.do?page=2), [국가기록원 '교복의 변천'(2014-02)](https://theme.archives.go.kr/next/monthly/viewMain.do?year=2014&month=02).

## 표 1. 판정표

행 단위: 의상 라벨 1개 = 1행(55행). 머리·얼굴 고정값 = 인물당 1행(16행). 단역 고정 문구 = 1행씩(7행). 신규 지정 1행(최 계장 1950년대 회상). 합계 79행. 건수는 문서 끝 절.

| 인물 | 의상(라벨) | 판정(맞음/수정 권장/미확인) | 근거 요약 | 출처 URL |
|---|---|---|---|---|
| 은주 | 큰 남색 점퍼·해진 바지·목장갑(+영문의 고무장화) | 미확인 (3-6·3-7 계절 부적합 → 표 2) | 난지도 사진의 '어둡고 두꺼운 옷'과 맞음. 아이가 고물을 주울 때의 차림을 직접 다룬 자료는 없음. 3-6(5월 말~6월)·3-7(6월 초)에도 이 점퍼가 배정됨(6월 평균 22.7°C) | [S22](https://www.seoulsolution.kr/sites/default/files/policy/%EB%82%9C%EC%A7%80%EB%8F%84%EA%B7%B8%ED%96%A5%EA%B8%B0%EB%A5%BC.pdf), [S19](https://en.wikipedia.org/wiki/Seoul) |
| 은주 | 흰 블라우스·감색 치마(학교) | 수정 권장(영문) | 국민학교는 자유복이라 블라우스+치마 자체는 문제없음. 그런데 영문이 'navy pleated skirt'와 '(her school clothes)'를 함께 써서 교복(세라복 등)으로 그려질 위험이 큼 | [S23](https://theme.archives.go.kr/next/education2010/wear05.do), [S24](https://www.khan.co.kr/article/201708132131005) |
| 은주 | 빌린 흰 원피스(무대) | 수정 권장(영문) | 청소년 대회 연주복 자료는 미확인. 대본 3화 S#17은 '소매가 손등을 반쯤 덮는다'(긴 소매)인데 영문에 소매가 빠져 있음 | 대본 3화 S#17 |
| 은주 | 남색 점퍼·회색 손뜨개 목도리·손끝 자른 목장갑(겨울) | 미확인 (계절 맞음) | 1월 평균 −2.0°C, 최저 −5.5°C라 두꺼운 차림이 맞음. 물건 하나하나의 1987년 근거는 없음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 은주 | 빛바랜 하늘색 반소매 셔츠·해진 바지(여름) | 미확인 (계절 맞음, 영문 신발 → 표 2) | 7월 평균 25.3°C. 영문에 고무장화가 고정되어 있음. 3-8~3-15는 공방·실내 씬이라 장화는 쓰레기 산에서만 신는 편이 자연스러움(추측). 운동화는 1960년경부터 대중화 | [S19](https://en.wikipedia.org/wiki/Seoul), [S17](https://encykorea.aks.ac.kr/Article/E0003567) |
| 은주 | 짙은 남색 연주 드레스(2003, 어른) | 미확인 | 2003년 연주자 드레스 자료는 찾지 못함. 시대색이 약한 옷이라 위험은 낮음 | — |
| 은주 | (머리·얼굴) 앞머리 없이 긴 머리를 고무줄 하나로 낮게 묶음, 잔머리, 소리굽쇠 목걸이 | 미확인 (규정상 충돌 없음) | 국민학교는 두발 자유형이고 1982년 두발 자유화가 있었으므로 규정과 충돌하지 않음. 1987년 여자아이 머리 모양의 직접 사진 근거는 없음 | [S23](https://theme.archives.go.kr/next/education2010/wear05.do), [S5](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do) |
| 동민 | 물려받은 큰 운동복(초록) | 맞음 (형태) / 색은 미확인 | 1980년대 동네 운동복은 상하의에 옆선 한 줄이 있는 형태였고(서울신문 2004 회고), 1970년대 말 츄리닝은 헐렁했음(경향 2003). 초록 색의 근거는 없음 | [S9](https://www.seoul.co.kr/news/life/2004/03/17/20040317024004), [S10](https://www.khan.co.kr/article/200307101630251) |
| 동민 | 물려받은 누빈 갈색 점퍼·털모자(겨울) | 미확인 (계절 맞음; 3-32 배정 오류 → 표 2) | 1월 기온과 맞음. 그런데 3-32 몽타주(1988년 가을 이사·등교)에도 이 겨울옷이 배정됨 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 동민 | 초록 반소매 운동복·반바지(여름) | 수정 권장(영문) | 'short-sleeved tracksuit top'은 앞지퍼 재킷인 트레이닝 상의와 반소매가 섞인 말이라 그림이 어긋날 수 있음. 반소매 면 티(체육복풍)로 풀어 쓰는 편이 안전(추측). 계절은 맞음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 동민 | 흰 반소매 남방·감색 반바지(제일 좋은 옷) | 미확인 (2-18 계절 경계 → 표 2) | 2-18은 1988년 4월 셋째 주(4월 평년 평균 12.6°C, 최고 17.9°C). 실내라 그릴 수는 있지만 반소매에 반바지는 쌀쌀함(추측). 같은 날 저녁인 2-19에는 평상복으로 돌아가 있어 연속성이 깨짐 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 동민 | 흰 반소매 남방·감색 반바지·빨간 손수건(본선) | 미확인 (계절 맞음) | 7월 23일 한여름이라 맞음. 나들이옷의 1988년 직접 근거는 없음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 동민 | 검은 티셔츠·청바지(2003, 어른) | 미확인 | 2003년에는 큰 로고 청바지 같은 세미복고가 유행(한국일보 2003). 무지 검은 티와 청바지는 그 시대에도 무리 없음. 스키니진으로 그려질 위험은 표 3 | [S25](https://www.hankookilbo.com/news/article/200301100084193889) |
| 동민 | (머리·얼굴) 아주 짧은 까까머리, 앞니 빠짐, 무릎 반창고 | 미확인 (1960~70년대 근거 있음) | 1960~70년대 아이들이 이발소에서 빡빡머리·상고머리로 깎았다는 근거는 있음. 1987년 국민학생의 직접 근거는 없음. 모던 페이드컷으로 그려질 위험은 표 3 | [S20](https://www.khan.co.kr/article/201006271815342) |
| 만석 | 낡은 야전상의·목수건·고무장화 | 수정 권장 (영문 + 본선 날 배정) | 1987~88년 야전상의는 얼룩무늬 이전 것이다(얼룩무늬는 1991-11-23부터). 영문 'olive army field jacket'만 쓰면 얼룩무늬나 패치 달린 미군 M-65로 그려질 위험이 있음. 대본 3화 S#16에서 야전상의를 입는 것은 의도이므로 유지. 다만 같은 씬 섬사람들은 '고무장화 대신 운동화'인데 만석은 3-16~3-29에 고무장화가 그대로 배정됨. 민간인이 야전상의를 입은 실태와 단속 여부는 미확인 | [S1](https://encykorea.aks.ac.kr/Article/E0006624), 대본 3화 S#16 |
| 만석 | 1970년대 극장 악단 흰 재킷·나비넥타이(회상) | 미확인 | 극장 쇼 악단 복장의 국내 자료는 찾지 못함(쇼단 회고 기사에도 복장 서술 없음). 1970년대 양복의 넓은 깃·피크 라펠과 넓은 바지 부리는 확인됨 → 영문 보강안은 표 2 | [S28](https://www.khan.co.kr/article/201208241932115), [S12](https://encykorea.aks.ac.kr/Article/E0035532) |
| 만석 | 다린 흰 셔츠·검은 바지(2003, 백발) | 미확인 | 시대색이 약한 옷이라 위험은 낮음 | — |
| 만석 | (머리·얼굴) 챙이 해진 국방색 작업모, 흰머리 섞인 짧은 머리, 수염 자국 | 미확인 | 국방색 작업모의 1980년대 민간 착용 근거는 찾지 못함. 새마을 모자를 쓰고 작업하는 사진은 2005년 것뿐(검색 요약). 로고 달린 야구모자로 그려질 위험은 표 3 | — |
| 곽 영감 | 톱밥 묻은 캔버스 앞치마·팔토시 | 미확인 (영문 속옷 층 공백, 본선 날 배정 → 표 2) | 목공 앞치마와 팔토시의 1987년 근거는 찾지 못함. 영문에 앞치마 안 옷이 없어 GPT가 임의로 채움. 이 옷이 3-18·3-22·3-24·3-27(본선 무대 옆, 7월)에도 그대로 배정됨. 대본은 본선 날 복장을 정하지 않았음(무대 옆 접이식 의자, 귀에 연필, 돋보기만). 여름(3-9·3-15) 변형도 없음 | 대본 3화 S#18·S#22 |
| 곽 영감 | 앞치마 위 회색 털조끼·털모자(겨울) | 미확인 (계절 맞음) | 2-17(1988년 1~3월) 공방 장면. 1월 기온과 맞음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 곽 영감 | 깨끗한 갈색 카디건(2003) | 미확인 | 시대색이 약한 옷이라 위험은 낮음 | — |
| 곽 영감 | (머리·얼굴) 짧은 흰 스포츠머리, 돋보기를 이마에, 귀에 연필, 굽은 약지·새끼손가락 | 미확인 | 바이블 설정. 머리는 상고·스포츠형 계열로, 1960~70년대 이발소 근거만 있음 | [S20](https://www.khan.co.kr/article/201006271815342) |
| 선영 | 구겨진 흰 셔츠·카디건·긴 플레어스커트 | 맞음 (블라우스+스커트 조합) / 긴 플레어 길이는 미확인 | 1984·1986년 여대 졸업앨범에서 블라우스+스커트 조합이 선호됨. 다만 이 논문은 전체 기간에 무릎 길이 타이트스커트가 더 많다고 함. 3-8·3-10(6월) 여름 씬에도 카디건 차림 그대로 → 표 2 | [S21](https://scholarworks.sookmyung.ac.kr/handle/2020.sw.sookmyung/9017) |
| 선영 | 검은 연주복(무대) | 미확인 | 1988년 지휘자·연주자 복장의 국내 자료는 찾지 못함. 영문 'plain black concert outfit'은 아래가 바지인지 치마인지 정하지 않음(characters.json은 long_skirt) | — |
| 선영 | 베이지 더플코트·목도리(늦가을~겨울) | 미확인 (계절 맞음) | 1980~90년대 학생들 사이에서 '떡볶이 코트'가 인기였다는 서술은 검색 요약에만 있고 출처 페이지를 특정하지 못함. 11월 평균 7.5°C, 1월 −2.0°C | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 선영 | 단정한 감색 정장(2003, 음악 교사) | 미확인 | 시대색이 약한 옷이라 위험은 낮음 | — |
| 선영 | (머리·얼굴) 볼륨 있는 반곱슬 파마 단발, 부풀린 앞머리, 크고 동그란 금테 안경 | 맞음 (머리) / 안경은 미확인 | 1980년대 이층 보브, 중반의 풀어 헤친 웨이브 파마, 무스·스프레이로 세운 앞머리가 확인됨. 1980년대 국내 안경 유행 자료는 찾지 못함(해외 자료에는 큰 테가 유행) | [S6](https://encykorea.aks.ac.kr/Article/E0018097) |
| 최 계장 | 회색 양복·넥타이·서류 봉투 | 미확인 (7월 씬 여름 변형 없음 → 표 2) | 공무원 근무복(간소복·새마을복)이 1996년까지 있었다는 기록은 있으나 1980년대 실태는 서술이 없음 → 구청 계장이 양복을 입었는지 근무복을 입었는지는 미확인. 3-12~3-14·3-20~3-29(7월)에 넥타이 맨 모직 양복 그대로. 대본 3-12는 선풍기가 돌아가는 무더운 사무실 | [S13](https://theme.archives.go.kr/next/koreaOfRecord/simpleClothes.do), [S19](https://en.wikipedia.org/wiki/Seoul), 대본 3화 S#12 |
| 최 계장 | 회색 양복 위 감색 오버코트(겨울) | 미확인 (계절 맞음) | 2-15(1988년 1월) | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 최 계장 | 넥타이 없는 회색 양복(2003) | 미확인 | 대본 3화 S#34와 일치. 시대 근거는 없음 | 대본 3화 S#34 |
| 최 계장 | (머리·얼굴) 반짝이는 7:3 포마드 가르마, 두꺼운 검은 뿔테, 흰 손수건 | 미확인 | 1980년대 중년 공무원의 머리·안경 자료는 찾지 못함 | — |
| 최 계장 | (회상, 1950년대 어린 시절) 의상 미지정 | 수정 권장(신규 지정) | 대본 3-12 Insert: 판잣집 양철 지붕 아래 쪼그린 아이의 맨발. 의상 라벨이 없어 GPT가 임의로 그림. 1950년대 판잣집 재료(생철·깡통·천막천)는 확인됨. 옷은 미군 구호물자·군복 재생옷이 흔했다는 서술이 검색 요약에만 있음(출처 페이지 특정 못 함) → 추측으로 안 제시(표 2). 이 행은 의상 라벨 55개에 포함되지 않는 추가 행 | [S26](https://theme.archives.go.kr/next/koreaOfRecord/panjaChon.do), 대본 3화 S#12 |
| 태준 | 사립학교 교복(감색 재킷·넥타이) | 미확인 (그럴듯함, 영문 보강 → 표 3) | 1986년 2학기부터 학교장 재량으로 교복 재허용. 새 교복은 개성 있고 밝은 색의 다양한 형태였고, 대부분 남학생은 상의+바지 정장. 블레이저형이 대세가 된 것은 1990년대이고, 1993년에도 교복 학교는 약 83%. 그러니 1987년 강남 사립중의 감색 재킷+넥타이는 가능하지만 직접 근거는 없음. 2-4·2-18 객석 단역을 '모두 교복'으로 그리면 1987~88년 실제보다 교복이 많아 보임(추측: 교복과 사복을 섞는 편이 고증에 가까움) | [S4](https://encykorea.aks.ac.kr/Article/E0005480), [S5](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do) |
| 태준 | 검은 연주복 | 미확인 | 1980년대 청소년 오케스트라 대회 복장 자료는 찾지 못함 | — |
| 태준 | 검은 정장 연주복(2003, 어른) | 미확인 | 시대색이 약한 옷이라 위험은 낮음 | — |
| 태준 | (머리·얼굴) 반듯한 7:3 옆가르마, 이마 드러냄 | 미확인 (규정상 충돌 없음) | 1982년 두발 자유화 이후라 가르마 머리가 가능함 | [S5](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do) |
| 미자 | 빨간 트레이닝 상의 | 맞음 (형태) / 빨강은 미확인 | 1980년대 동네 운동복은 옆선 한 줄 있는 상하의였음. 1987년 4월~11월 장면에 쓰여 계절 무리 없음 | [S9](https://www.seoul.co.kr/news/life/2004/03/17/20040317024004) |
| 미자 | 빨간 누빔 점퍼(겨울) | 미확인 (계절 맞음) | 1월 기온과 맞음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 미자 | 빨간 반소매 티(여름) | 미확인 (계절 맞음) | 7월 기온과 맞음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 미자 | 새것 같은 빨간 트레이닝 위아래(제일 좋은 옷) | 맞음 (형태) | 상하의를 맞춘 운동복은 1980년대 회고에 나옴(노란 상하의 등). 2-18은 4월이라 계절 무리 없음. 같은 날 저녁 2-19에는 평상복 '빨간 트레이닝 상의'로 바뀌어 있음 → 표 2(연속성) | [S9](https://www.seoul.co.kr/news/life/2004/03/17/20040317024004) |
| 미자 | 새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선) | 맞음 (형태) / 계절 주의 | 형태는 위와 같음. 7월 23일(평년 최고 29.0°C)에 긴소매 상하의라 더워 보임. 인물이 고른 '제일 좋은 옷'이라 유지할 수 있음. 1988년 공연장 냉방 여부는 미확인 | [S9](https://www.seoul.co.kr/news/life/2004/03/17/20040317024004), [S19](https://en.wikipedia.org/wiki/Seoul) |
| 미자 | 감색 트레이닝복·호루라기·출석부(2003, 체육 교사) | 맞음 | 2003년은 트레이닝복이 주류 패션이 된 해. 2003년 트레이닝복은 날렵한 핏에 옆선 있는 9~10부 바지 → 1980년대 헐렁한 츄리닝과 반대로 그려야 함(표 3) | [S10](https://www.khan.co.kr/article/200307101630251), [S11](https://www.hankookilbo.com/news/article/200312190021393066) |
| 미자 | (머리·얼굴) 가위로 짧게 친 숏단발, 뻗친 앞머리, 코 반창고 | 미확인 (규정상 충돌 없음) | 1982년 두발 자유화 이후. 1987년 중학생 머리의 직접 근거는 없음 | [S5](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do) |
| 덕수 | 늘어난 흰 러닝셔츠 위 체크 남방 | 미확인 (흰 러닝셔츠는 약한 근거) | 흰 백양 러닝셔츠가 어린 시절 속옷이었다는 개인 회고(연대 미상)만 있음. 2-6(11월 초, 평년 최고 11.9°C) 둑길 씬에서도 남방 한 겹이라 얇음(추측) | [S18](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0001611657), [S19](https://en.wikipedia.org/wiki/Seoul) |
| 덕수 | 체크 남방 위 회색 털스웨터(겨울) | 미확인 (계절 맞음) | 1월 기온과 맞음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 덕수 | 흰 러닝셔츠·반바지(여름) | 미확인 (계절 맞음) | 위와 같은 약한 근거. 1970년대 말 '러닝셔츠+헐렁한 츄리닝' 차림의 회고는 있음 | [S18](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0001611657), [S10](https://www.khan.co.kr/article/200307101630251) |
| 덕수 | 단추를 목까지 잠근 체크 남방·빨간 손수건(본선) | 미확인 | 대본 2화 S#18(예선)의 '체크 남방 단추를 목까지'를 본선에 다시 쓴 것. 영문은 긴 바지라 7월에 무리는 없음 | 대본 2화 S#18 |
| 덕수 | 꽃무늬 앞치마(2003, 국밥집) | 미확인 | 대본 3화 S#34 '순례 할머니의 꽃무늬 앞치마를 둘렀다'와 일치 | 대본 3화 S#34 |
| 덕수 | (머리·얼굴) 짧은 스포츠머리, 단추가 한 칸씩 어긋난 남방 | 미확인 | 상고·스포츠형 계열. 1960~70년대 이발소 근거만 있음 | [S20](https://www.khan.co.kr/article/201006271815342) |
| 순례 할머니 | 몸뻬 바지·꽃무늬 앞치마 | 맞음 (몸뻬) / 영문은 수정 권장 | 광복 뒤 몸뻬가 도시·농촌의 노동복·일상복으로 자리 잡았고, 고무줄 허리에 합성섬유임이 확인됨. 영문 'momppe'는 GPT가 모르는 말이라 형태를 풀어 써야 함. 잔꽃무늬는 위키 계열 서술뿐이라 추측 | [S2](https://encykorea.aks.ac.kr/Article/E0079810) |
| 순례 할머니 | 솜 누빈 조끼·털목도리(겨울) | 미확인 (계절 맞음) | 1월 기온과 맞음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 순례 할머니 | 외출용 자주색 블라우스·몸뻬, 접은 앞치마를 손에(본선) | 수정 권장 (잠정 의상) | 몸뻬는 '일바지'(노동복)임. 1970년대 이후 한복은 큰일 있는 외출·명절 옷이었고, 1989년 잡지는 80년대 할머니가 쪽을 찌고 한복을 일상복으로 입었다고 전함 → 서울 한복판 대회 나들이에 몸뻬보다 여름 한복이 시대에 맞을 가능성이 큼(추측). 대본 3화 S#16은 '제일 좋은 옷'이라고만 써서 충돌 없음 | [S2](https://encykorea.aks.ac.kr/Article/E0079810), [S15](https://theme.archives.go.kr/next/education2010/wear01.do), [S7](https://www.khan.co.kr/article/202302281813001) |
| 순례 할머니 | 자주색 외출 블라우스·몸뻬(2003, 객석) | 미확인 | 2003년 노년 여성의 외출복 자료는 찾지 못함 | — |
| 순례 할머니 | (머리·얼굴) 낮게 진 흰 쪽진 머리(비녀 대신 검은 핀), 굽은 등, 국자 | 맞음 (쪽진 머리) / 핀은 수정 권장(경미) | 80년대 할머니들이 여전히 쪽을 쪘다는 1989년 잡지 근거가 있음. 쪽은 비녀로 고정하는 것이 기본(검색 요약). '검은 핀'만 쓰면 GPT가 현대식 똥머리로 그릴 위험이 있음. 중년(미자 엄마 세대)은 오래가는 파마가 대세였음 | [S7](https://www.khan.co.kr/article/202302281813001), [S27](https://encykorea.aks.ac.kr/Article/E0025100), [S8](https://www.khan.co.kr/article/200011231651001) |
| 봉구 | 노란 러닝셔츠·반바지 | 미확인 | 러닝셔츠는 속옷이고, 흰색이 전형이었다는 약한 회고만 있음. 노란 민소매 상의의 1988년 근거는 없음. 여름 평상복(3-9·3-10·3-14·3-33)으로는 무리 없음 | [S18](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0001611657) |
| 봉구 | 노란 러닝셔츠·반바지·빨간 손수건(본선) | 수정 권장 [확정 변경, 사용자 승인 필요] | 본선 규칙은 '제일 좋은 옷'인데 속옷(러닝셔츠) 차림. 대본 3화 S#16의 섬사람들은 다림질한 셔츠·장롱 속 블라우스로 차려입음 → 봉구만 속옷이면 어긋남(추측). 노란색은 유지하고 반소매 셔츠로 바꾸면 '옷 색 하나' 원칙을 지킬 수 있음 | 대본 3화 S#16, [S18](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0001611657) |
| 봉구 | (머리·얼굴) 까까머리, 넓적한 얼굴 | 미확인 (1960~70년대 근거 있음) | 동민 행과 같음 | [S20](https://www.khan.co.kr/article/201006271815342) |
| 영란 | 분홍 반소매 블라우스·감색 치마 | 미확인 (계절 맞음) | 1988년 6~7월 여름 씬. 여자아이 옷의 직접 근거는 없음 | [S19](https://en.wikipedia.org/wiki/Seoul) |
| 영란 | 분홍 반소매 블라우스·감색 치마·빨간 손수건(본선) | 미확인 (계절 맞음) | 위와 같음. 블라우스+치마는 나들이옷으로도 자연스러움(추측) | — |
| 영란 | (머리·얼굴) 양갈래로 묶은 머리 | 미확인 | 1970년대 여학교에서 '단발·묶기·땋기'만 허용됐다는 회고가 있어 묶은 머리 자체는 흔했을 것(추측). 1988년 국민학생 근거는 없음 | [서울시 미디어허브(1970년대 교복 회고)](https://mediahub.seoul.go.kr/archives/195602) |
| 경호 | 파란 티·반바지 | 미확인 (계절 맞음) | 직접 근거 없음. 1980년대 셔츠에 영문자·만화 캐릭터를 크게 넣었다는 회고가 있음(아이 옷 한정 서술은 아님)(무지 티 대신 고려 가능, 단 글자 없는 이미지 규칙 때문에 무지가 안전) | [S25](https://www.hankookilbo.com/news/article/200301100084193889) |
| 경호 | 파란 티·반바지·빨간 손수건(본선) | 미확인 | 본선 '제일 좋은 옷'으로 평상 티는 약간 어색함(추측). 바꾸지는 않음 | — |
| 경호 | (머리·얼굴) 바가지 머리 | 미확인 | 바가지머리는 1967년 여성 유행으로만 확인됨. 1980년대 남자아이 근거는 없음. 집에서 깎은 머리로는 그럴듯함(추측) | [S6](https://encykorea.aks.ac.kr/Article/E0018097) |
| 경민 | 주황 티·반바지 | 미확인 (계절 맞음) | 경호 행과 같음 | — |
| 경민 | 주황 티·반바지·빨간 손수건(본선) | 미확인 | 경호 행과 같음 | — |
| 경민 | (머리·얼굴) 바가지 머리 | 미확인 | 경호 행과 같음 | [S6](https://encykorea.aks.ac.kr/Article/E0018097) |
| 순이 | 꽃무늬 원피스 | 미확인 (계절 맞음) | 직접 근거 없음 | — |
| 순이 | 꽃무늬 원피스·빨간 손수건(본선) | 미확인 | 나들이옷으로 자연스러움(추측) | — |
| 순이 | (머리·얼굴) 단발, 빨간 머리띠 | 미확인 | 직접 근거 없음 | — |
| 석이 | 물려받은 큰 반소매 티(어깨가 흘러내림)·큰 모자 | 수정 권장(영문) | 시대 근거는 없음(미확인). 영문 'slipping off one shoulder'는 오프숄더 패션처럼 그려질 수 있어 style_guide 7절(아동 노출 없음)과 부딪칠 위험이 있음. 'a big cap'은 로고 달린 현대 야구모자로 그려질 위험이 있음 | style_guide.md 7절 |
| 석이 | 물려받은 큰 반소매 티(어깨가 흘러내림)·큰 모자·빨간 손수건(본선) | 수정 권장(영문) | 위와 같음 | style_guide.md 7절 |
| 석이 | (머리·얼굴) 큰 모자 밑 까까머리, 빨간 볼 | 미확인 (1960~70년대 근거 있음) | 동민 행과 같음 | [S20](https://www.khan.co.kr/article/201006271815342) |
| 단역 | 갈고리 아주머니: 머릿수건, 어둡고 두꺼운 작업복, 긴 쇠갈고리 | 맞음 (옷·머릿수건) / 도구는 미확인 | 난지도 하역 사진의 머릿수건·어둡고 두꺼운 옷과 일치. 문헌으로 확인된 폐품 수집 도구는 망태기·집게, 사진으로는 등에 진 대바구니 → 등짐을 더하면 고증에 가까움. '긴 쇠갈고리' 자체는 미확인 | [S22](https://www.seoulsolution.kr/sites/default/files/policy/%EB%82%9C%EC%A7%80%EB%8F%84%EA%B7%B8%ED%96%A5%EA%B8%B0%EB%A5%BC.pdf), [S3](https://encykorea.aks.ac.kr/Article/E0068876) |
| 단역 | 미자 엄마: 파마한 짧은 머리, 어두운 작업복, 빨간 카디건 | 맞음 (파마) | 중년 여성의 오래가는 파마 확인. 옷은 미확인 | [S8](https://www.khan.co.kr/article/200011231651001) |
| 단역 | 집하장 아저씨: 머리에 수건, 고무 앞치마, 작업 장갑 | 미확인 | 직접 근거 없음. 'work gloves'는 표 3 참조 | — |
| 단역 | 전당포 주인: 이마의 확대경, 어두운 조끼, 흰 셔츠, 토시 | 미확인 | scene_presets에도 '근거 없음, 제안'으로 적혀 있음 | — |
| 단역 | 과장(구청): 마른 50대, 회색 양복, 줄 달린 돋보기 | 미확인 | 안경 줄의 1980년대 국내 근거는 없음. 근무복(간소복) 여부도 미확인(최 계장 행 참조) | [S13](https://theme.archives.go.kr/next/koreaOfRecord/simpleClothes.do) |
| 단역 | 사회자: 1980년대 연한 회색 양복, 나비넥타이, 줄 달린 마이크 | 미확인 | 직접 근거 없음 | — |
| 단역 | 엄마 한미숙(회상): 빛바랜 꽃무늬 블라우스, 얼굴 금지 | 미확인 | 직접 근거 없음 | — |

## 표 2. 수정 권장 목록

라벨을 바꾸는 경우에는 `characters.json` → `outfits_en.json` → `outfit_schedule.json` 순서로 같은 문자열을 맞춘다(CONTINUE.md 27행 절차). '영문만'이라고 적은 항목은 `outfits_en.json` 값만 바꾼다.

| # | 대상 | 무엇을 어떻게 (한국어 라벨 수정안) | 영어 문장 수정안 | 이유 |
|---|---|---|---|---|
| 1 | 만석 '낡은 야전상의·목수건·고무장화' | 라벨 유지, 영문만 | `a worn, faded plain solid olive-drab 1980s Korean army field jacket (no camouflage pattern, no patches, no insignia, no name tape), a cotton towel around the neck, worn dark work trousers, rubber boots` | 얼룩무늬 야전상의는 1991-11-23부터라 1987~88년은 단색이어야 함([S1](https://encykorea.aks.ac.kr/Article/E0006624)). 'army field jacket'만 쓰면 얼룩무늬나 미군 패치로 그려질 위험이 있음 |
| 2 | 만석, 본선 날 3-16~3-29 | 새 라벨 `낡은 야전상의·다린 셔츠·운동화(본선)`를 만들어 3-16~3-29에 배정 | `the same worn plain solid olive-drab field jacket (no camouflage, no insignia), collar pulled closed, over a pressed collared shirt, dark trousers, worn canvas sneakers instead of rubber boots, no towel` | 대본 3화 S#16: 야전상의는 그대로 입고 깃을 여밈. 같은 씬 섬사람들은 '고무장화 대신 운동화'. 지금 일정표는 고무장화·목수건까지 그대로 들어감 |
| 3 | 은주 '흰 블라우스·감색 치마(학교)' | 라벨 유지, 영문만 | `her own plain everyday clothes, not a school uniform: a faded white cotton blouse and a plain navy skirt` | 국민학교는 자유복([S23](https://theme.archives.go.kr/next/education2010/wear05.do)). 'pleated'와 'school clothes'가 겹치면 교복(세라복 등)으로 그려질 위험이 있음 |
| 4 | 은주 '빌린 흰 원피스(무대)' | 라벨 유지, 영문만 | `a borrowed plain white cotton dress, a little too big for her, long sleeves that keep sliding down to half cover the backs of her hands, hem well below the knee, no frills, no lace` | 대본 3화 S#17의 소매 묘사를 반영. 아동 인물이 드레스·가운처럼 꾸며지지 않게(style_guide 7절) |
| 5 | 은주 '빛바랜 하늘색 반소매 셔츠·해진 바지(여름)' | 라벨 유지, 영문만 | `a faded light-blue short-sleeved cotton shirt, worn trousers with frayed knees, worn canvas sneakers (rubber boots and cotton work gloves only when working on the trash hill)` | 배정된 씬 3-8~3-15·3-33이 공방·국밥집·실내라 장화를 늘 신을 이유가 없음(추측). 운동화는 1960년경부터 대중화([S17](https://encykorea.aks.ac.kr/Article/E0003567)) |
| 6 | 은주 3-6(5월 말~6월)·3-7(6월 초) | 일정표에 `빛바랜 하늘색 반소매 셔츠·해진 바지(여름)` 추가(쓰레기 산 장면이면 점퍼 대신 셔츠+목장갑+장화) | (기존 문장) | 6월 평년 평균 22.7°C, 최고 27.6°C([S19](https://en.wikipedia.org/wiki/Seoul)). 큰 남색 점퍼는 무거움. 3-1~3-5(5월)는 아침·저녁 장면이 많아 점퍼를 유지해도 됨(추측) |
| 7 | 동민 '초록 반소매 운동복·반바지(여름)' | 라벨을 `초록 반소매 체육복 티·반바지(여름)`로 바꾸는 것을 검토 | `a green short-sleeved cotton gym T-shirt and matching green shorts, worn canvas sneakers` | 'short-sleeved tracksuit top'은 지퍼 재킷인지 티인지 모호함 |
| 8 | 동민·미자 2-19(2-18과 같은 날 저녁) | 일정표 2-19에 2-18과 같은 '제일 좋은 옷' 배정 | (기존 문장) | 연속성 오류. 예선 당일 저녁에 평상복으로 바뀌어 있음 |
| 9 | 동민 2-18(1988년 4월 셋째 주, 실내) | (선택) 라벨 유지. 그리면서 흰 무릎 양말을 더하거나, 긴소매 남방 변형 `흰 긴소매 남방·감색 반바지(제일 좋은 옷, 봄)`을 새로 만듦 | `his best clothes: a white long-sleeved button shirt, navy shorts, white knee socks, sneakers` | 4월 평년 평균 12.6°C·최고 17.9°C. 실내라 지금 그대로도 그릴 수 있음. 경계 사례라 선택 사항 |
| 10 | 3-32 몽타주(1988년 가을 이사·등교) | 동민의 겨울옷 배정을 지우고 기본 `물려받은 큰 운동복`으로. `_kids`의 3-32 'base'(여름옷)는 빼거나 가을용 긴소매를 따로 만듦 | (기존 문장) | 3-32 첫 컷들은 1988년 가을(9~10월, 평년 평균 21.7~15.0°C). 겨울 누빔 점퍼·털모자도, 러닝셔츠·반바지도 맞지 않음 |
| 11 | 곽 영감 '톱밥 묻은 캔버스 앞치마·팔토시' | 라벨 유지, 영문만 | `a canvas work apron dusted with sawdust over a faded gray long-sleeved work shirt and dark work trousers, cloth arm sleeves, a pencil behind his ear` | 앞치마 안 옷이 비어 있어 GPT가 씬마다 다르게 채움. 셔츠 색은 추측 |
| 12 | 곽 영감, 여름(3-9·3-15)과 본선(3-18·3-22·3-24·3-27) | 새 라벨 `앞치마·반소매 작업 셔츠(여름)`, `다린 흰 반소매 셔츠·회색 바지(본선)` | 여름: `a canvas work apron over a faded short-sleeved work shirt, dark work trousers, cloth arm sleeves` / 본선: `his going-out clothes: a pressed white short-sleeved shirt buttoned to the top, gray trousers, a pencil behind his ear, reading glasses on his nose` | 7월 평년 최고 29.0°C. 본선 날은 섬사람들이 모두 차려입었는데(대본 3화 S#16) 영감만 작업 앞치마임. 대본에는 본선 복장 지시가 없어 추측 제안 |
| 13 | 선영, 여름 3-8·3-10 | 새 라벨 `구겨진 흰 반소매 블라우스·긴 플레어스커트(여름)` | `a wrinkled white short-sleeved blouse and a long flared skirt, no cardigan` | 6월 말 여름 장면에 카디건 |
| 14 | 최 계장, 7월 3-12~3-14 | 새 라벨 `흰 반소매 와이셔츠·넥타이, 양복 상의는 의자에(여름)` | `a white short-sleeved dress shirt with a tie, gray suit trousers, the gray suit jacket hung on the chair back or over his arm` | 대본 3-12의 선풍기 돌아가는 무더운 사무실. 1980년대 공무원 여름 차림의 근거는 없음(추측). 본선 객석(3-20 이후)은 양복 상의를 입어도 됨. 근무복(간소복·새마을복)은 1996년까지 있었지만 1980년대 실태는 미확인([S13](https://theme.archives.go.kr/next/koreaOfRecord/simpleClothes.do)) |
| 15 | 최 계장 1950년대 회상(3-12 Insert) | 새 라벨 `기워 입은 헐렁한 옷·맨발(1950년대 회상)` | `a small boy in 1950s Seoul, an oversized much-patched faded shirt and shorts cut down from adult clothes, barefoot, crouching under a rusty tin-sheet roof, desaturated colors` | 지금은 의상이 없음. 판잣집 재료(생철·깡통)는 확인됨([S26](https://theme.archives.go.kr/next/koreaOfRecord/panjaChon.do)). 옷차림은 추측 |
| 16 | 만석 '1970년대 극장 악단 흰 재킷·나비넥타이(회상)' | 라벨 유지, 영문 보강 | `a 1970s Korean theater show band uniform: a white jacket with wide peaked lapels, a white shirt, a black bow tie, dark flared trousers` | 1970년대 넓은 피크 라펠·넓은 바지 부리는 확인됨([S12](https://encykorea.aks.ac.kr/Article/E0035532)). 흰 재킷·나비넥타이 자체는 미확인. design/gen/character_prompts.md ⑤에도 같은 보강 필요 |
| 17 | 순례 할머니 '몸뻬 바지·꽃무늬 앞치마' 외 몸뻬가 든 모든 영문(4개) | 라벨 유지, 영문의 몸뻬 부분만 | `baggy elastic-waist Korean work trousers (momppe) in a small floral print, wide in the leg and gathered at the ankles` | GPT는 'momppe'를 모름. 형태는 [S2](https://encykorea.aks.ac.kr/Article/E0079810)에서 확인. 잔꽃무늬는 추측 |
| 18 | 순례 할머니 본선 '외출용 자주색 블라우스·몸뻬, 접은 앞치마를 손에' | 라벨을 `여름 한복(모시 치마저고리), 접은 앞치마를 손에(본선)`로 바꾸는 것을 검토(잠정 의상이라 승인 없이 교체할 수 있으나 확인 권장) | `her best going-out clothes: a light summer hanbok, a pale ramie jeogori jacket and a long full skirt, white rubber-soled shoes, holding her folded flower-pattern apron in one hand` | 몸뻬는 일바지([S2](https://encykorea.aks.ac.kr/Article/E0079810)). 한복은 큰일 있는 외출 옷([S15](https://theme.archives.go.kr/next/education2010/wear01.do)). 80년대 할머니는 쪽머리에 한복([S7](https://www.khan.co.kr/article/202302281813001)). 색·옷감은 추측. 몸뻬를 꼭 남긴다면 대안은 `자주색 블라우스·검정 긴 치마` |
| 19 | 순례 할머니 머리(style_guide 6절 고정 문구) | '비녀 대신 검은 핀' → '낮은 쪽에 수수한 비녀' **[확정 변경, 사용자 승인 필요]** | `white hair pulled back tightly into a low traditional bun (jjok) at the nape, fixed with a plain silver binyeo hairpin` | 쪽은 비녀로 고정하는 것이 기본([S27](https://encykorea.aks.ac.kr/Article/E0025100), 검색 요약). 'black hairpins'는 현대식 올림머리로 그려질 위험이 있음. G7 확정(바이블 기준 추천안 세부) 항목 |
| 20 | 봉구 '노란 러닝셔츠·반바지·빨간 손수건(본선)' | `노란 반소매 남방·반바지·빨간 손수건(본선)` **[확정 변경, 사용자 승인 필요]** | `his best clothes: a yellow short-sleeved button shirt and shorts, sneakers, a small red cloth neckerchief tied at the neck` | 본선 규칙은 '제일 좋은 옷'인데 속옷 차림. 대본 3화 S#16의 섬사람들은 다림질한 셔츠. 노란색은 그대로라 '옷 색 하나' 구분은 유지됨 |
| 21 | 석이 두 의상 | 라벨의 '(어깨가 흘러내림)' → '(소매가 팔꿈치 아래로)' **[확정 변경, 사용자 승인 필요: 섬 아이 디자인]** | `an oversized hand-me-down short-sleeved T-shirt, the sleeves hanging past his elbows and the hem down to his thighs, a too-big plain cotton cap with a soft brim and no logo` (본선은 끝에 `, a small red cloth neckerchief tied at the neck`) | 'slipping off one shoulder'는 오프숄더로 그려질 위험이 있음(style_guide 7절). 'big cap'은 로고 달린 야구모자로 그려질 위험이 있음 |
| 22 | 태준 '사립학교 교복(감색 재킷·넥타이)' | 라벨 유지, 영문만 | `a late-1980s Korean private middle-school uniform: a navy wool blazer with a small school badge, a white shirt, a plain dark tie, matching dark trousers in a loose straight cut; not a black high-collar uniform, not a sailor uniform` | 1986년 이후 재킷+바지 정장형([S4](https://encykorea.aks.ac.kr/Article/E0005480), [S5](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do)). 1983년 이전 검정 교복은 군복을 본뜬 형태였음([S24](https://www.khan.co.kr/article/201708132131005)) |
| 23 | 2-4·2-18 객석 단역 '교복(감색 재킷 등)' | scene_presets 문구를 '교복 학생과 사복 학생이 섞인 객석'으로 바꾸는 것을 검토 | `an audience of students, some in late-1980s school uniforms with jackets and some in their own casual clothes, and parents in 1980s outing clothes` | 1993년에도 교복 학교는 약 83%였음([S5](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do)). 대본이 '교복'이라고 썼으므로 참고 권장 수준 |
| 24 | 미자 '빨간 트레이닝 상의'·'새것 같은 빨간 트레이닝 위아래', 동민 '물려받은 큰 운동복' | 라벨 유지, 영문만 | 미자: `a loose-fitting red cotton-knit tracksuit top with a single contrasting stripe down each sleeve, zip front, no logo, dark trousers` / 동민: `an oversized hand-me-down loose green cotton-knit tracksuit with a single contrasting stripe down the sides, baggy at the knees, elastic cuffs, no logo` | 1980년대 동네 운동복은 줄 한 줄([S9](https://www.seoul.co.kr/news/life/2004/03/17/20040317024004)), 헐렁함([S10](https://www.khan.co.kr/article/200307101630251)). 줄 색은 확인된 예(노랑 바탕+검은 줄, 남색 바탕+빨간 줄)가 인물 색과 달라 'contrasting'으로만 씀. 흰 줄로 정하려면 추측 표시. 세 줄은 아디다스 상표라 피함 |
| 25 | 갈고리 아주머니(단역 고정 문구) | 등짐을 더함 | `a middle-aged Korean woman scavenger with a head scarf, dark padded work clothes, a large bamboo basket strapped on her back, holding a long iron hook` | 하역 사진의 등짐 대바구니([S22](https://www.seoulsolution.kr/sites/default/files/policy/%EB%82%9C%EC%A7%80%EB%8F%84%EA%B7%B8%ED%96%A5%EA%B8%B0%EB%A5%BC.pdf)), 넝마주이의 망태기([S3](https://encykorea.aks.ac.kr/Article/E0068876)) |
| 26 | 섬사람 군중 기본 옷(style_guide 7-1절, scene_presets의 '어둡고 두꺼운 작업복') | 2-1(9~10월)·1-14(5월)·3-6 등 따뜻한 달 군중은 '어두운 얇은 작업복, 머릿수건'으로 | `islanders in dark, worn, thin cotton work clothes with head scarves, a few red or blue tops` | [A] 사진(S22)은 촬영 연도·계절이 미상이라 '두꺼운 옷'을 모든 계절에 적용할 근거가 없음. 9월 평년 평균 21.7°C, 5월 18.2°C(S19). 추측 |
| 27 | 3-34 일정 | (의상 문제 아님) scene_presets 3-34에 dongmin이 두 번 들어 있음(어른 + 회상 Insert의 9세). 일정표는 첫 번째에만 적용되므로 지금은 의도대로 동작. 회상 쪽을 별도 id로 분리하면 안전 | — | 나중에 순서가 바뀌면 어른 동민이 9세 운동복을 입을 수 있음 |

### 계절 교차 점검 (평년값 S19, 1991–2020 기준. 1987~88년 실측 아님)

| 씬 | 시기 | 평년 평균/최고 °C | 배정 | 판정 |
|---|---|---|---|---|
| 2-14~2-17 | 1987 늦가을~1988 1~3월 | 1월 −2.0/2.1 | 겨울옷 일체 | 맞음. 만석만 겨울 변형 없음(야전상의+목수건, 추측상 무리 없음) |
| 2-18 | 1988-04 셋째 주, 실내 | 12.6/17.9 | 동민 반소매+반바지 | 경계(표 2 #9) |
| 2-19 | 2-18 같은 날 저녁 | — | 동민·미자 평상복 | 연속성 오류(표 2 #8) |
| 3-1~3-5 | 1988-05 | 18.2/23.6 | 은주 큰 남색 점퍼 | 대체로 허용(아침·저녁 장면 위주) |
| 3-6·3-7 | 5월 말~6월 초 | 22.7/27.6 | 은주 큰 남색 점퍼 | 수정 권장(표 2 #6) |
| 3-8~3-15 | 1988-06~07 | 22.7~25.3/27.6~29.0 | 아이들 여름옷 | 맞음. 선영 카디건(#13), 만석 3-10 야전상의, 곽 영감 여름 변형 없음(#12) |
| 3-12~3-14 | 1988-07 초 | 25.3/29.0 | 최 계장 양복+넥타이 | 수정 권장(#14) |
| 3-16~3-30 | 1988-07-23 | 25.3/29.0 | 본선 의상 | 아이들 맞음. 만석 장화(#2), 곽 영감 앞치마(#12), 미자 긴소매 상하의(유지 가능) |
| 3-32 | 1988 가을~ | 9월 21.7, 10월 15.0 | 동민 겨울옷, 섬 아이 여름옷 | 수정 권장(#10) |
| 3-34 | 2003 봄(월 미상) | 4~5월 12.6~18.2 | 2003 의상 | 맞음(봄옷으로 무리 없음) |

## 표 3. 시대 착오 위험 낱말 → 프롬프트 보강 문구

근거 칸에 '확인'이라고 쓴 것은 출처로 확인한 보강이다. '추측'은 안전을 위한 보강이며 고증으로 확인한 것이 아니다.

| 순위 | 위험 낱말(현재 영문) | GPT가 잘못 그리기 쉬운 것 | 보강 문구 제안 | 근거 |
|---|---|---|---|---|
| 1 | `army field jacket` (만석) | 얼룩무늬 전투복, 미군 M-65에 계급장·부대 패치·명찰 | `plain solid olive-drab 1980s Korean army field jacket, no camouflage pattern, no patches, no insignia, no name tape` | 확인: 얼룩무늬는 1991-11-23부터([S1](https://encykorea.aks.ac.kr/Article/E0006624)) |
| 2 | `tracksuit` (동민·미자 1987~88) | 현대 슬림핏 조거·애슬레저, 세 줄 브랜드 트랙탑 | `loose-fitting 1980s Korean cotton-knit tracksuit, baggy at the knees, elastic cuffs, a single contrasting side stripe, no logo` | 확인: 옆선 한 줄 동네 운동복([S9](https://www.seoul.co.kr/news/life/2004/03/17/20040317024004)), 헐렁한 츄리닝([S10](https://www.khan.co.kr/article/200307101630251)). 세 줄은 아디다스 상표라 금지 규칙에 걸림 |
| 2-1 | `tracksuit` (미자 2003) | 거꾸로 1980년대 헐렁한 츄리닝 | `slim-fit 2003-style navy tracksuit with side stripes on the sleeves and trousers, no logo` | 확인: 2003년 날렵한 핏, 옆선 9~10부 바지([S10](https://www.khan.co.kr/article/200307101630251)) |
| 3 | `school uniform` / `navy blazer` / `pleated skirt` (태준, 은주, 객석) | 1983년 이전 검정 차이나 칼라 교복이나 세라복, 2010년대 슬림 한국 교복·일본 교복, 국민학생 은주에게 교복 | 태준: `late-1980s Korean private-school uniform, navy blazer, plain tie, loose straight-cut trousers, not a black high-collar uniform, not a sailor uniform` / 은주: `her own plain everyday clothes, not a school uniform` | 확인: 1986 재허용, 재킷+바지 정장형([S4](https://encykorea.aks.ac.kr/Article/E0005480), [S5](https://theme.archives.go.kr/next/koreaOfRecord/schoolUniform.do)). 옛 교복은 군복형([S24](https://www.khan.co.kr/article/201708132131005)). 국민학교 자유복([S23](https://theme.archives.go.kr/next/education2010/wear05.do)) |
| 4 | `momppe` (순례) | 모르는 낱말이라 일반 바지나 일본풍 옷 | `baggy elastic-waist work trousers, wide in the leg and gathered at the ankles, synthetic fabric` (+ `small floral print`는 추측) | 확인: 형태·소재([S2](https://encykorea.aks.ac.kr/Article/E0079810)) |
| 5 | `sleeveless undershirt` (덕수·봉구) | 운동용 탱크톱, 농구 저지, 근육 셔츠 | `thin white cotton-knit sleeveless undershirt (Korean running shirt), stretched and slightly yellowed` | 약한 근거: 흰 백양 러닝셔츠 회고(연대 미상, [S18](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0001611657)) |
| 6 | `cotton work gloves` (은주 등) | 현대 반코팅 장갑(손바닥 빨강·파랑·회색 고무) | `plain white knitted cotton work gloves, no rubber coating` | 추측: 코팅 장갑의 국내 보급 시기는 미확인. 확인 전까지 코팅 없는 쪽이 안전 |
| 7 | `buzz cut` / `crew cut` (동민·봉구·석이·덕수) | 옆을 밀어 올린 페이드컷, 언더컷, 디자인 라인 | `very short uneven clipper cut, same length all over, no fade, no undercut` (덕수: `short back and sides, slightly longer on top, no fade`) | 일부 확인: 빡빡머리·상고머리([S20](https://www.khan.co.kr/article/201006271815342), 1960~70년대). 페이드 금지는 추측 |
| 8 | `big cap` / `work cap` (석이·만석) | 로고 달린 납작챙 야구모자, 스냅백 | 석이: `a too-big plain cotton cap with a soft curved brim, no logo` / 만석: `a faded olive cotton work cap with a short soft brim, no logo, no emblem` | 추측 |
| 9 | `slipping off one shoulder` (석이) | 오프숄더 패션(아동 노출 규칙 위반 위험) | `sleeves hanging past his elbows, hem down to his thighs` | style_guide 7절 |
| 10 | `permed bob with fluffy bangs` (선영) | 현대 비치 웨이브, 시스루 뱅 | `1980s permed bob with volume, loose waves, bangs lifted and set with mousse` | 확인: 1980년대 중반 웨이브 파마, 무스로 세운 앞머리([S6](https://encykorea.aks.ac.kr/Article/E0018097)) |
| 11 | `low bun held with black hairpins` (순례) | 현대 똥머리, 집게핀 | `low traditional bun (jjok) at the nape fixed with a plain binyeo hairpin` | 확인: 80년대 할머니 쪽([S7](https://www.khan.co.kr/article/202302281813001)). 비녀는 검색 요약([S27](https://encykorea.aks.ac.kr/Article/E0025100)) |
| 12 | 구청·공무원 단역이 점퍼를 입을 때 | 노란 민방위복 점퍼 | `no yellow civil-defense jacket` | 확인: 노란 민방위복은 2005년부터([S14](https://m.seoul.co.kr/news/life/2022/08/15/20220815500016)). 1987~88년 색은 미확인 |
| 13 | `1970s theater band uniform: white jacket` (만석 회상) | 요리사복, 해군 정복, 1990년대 이후 좁은 라펠 | `white jacket with wide peaked lapels, dark flared trousers` | 일부 확인: 1970년대 넓은 피크 라펠·넓은 바지 부리([S12](https://encykorea.aks.ac.kr/Article/E0035532)) |
| 14 | `jeans` (동민 2003) | 2010년대 스키니진, 찢어진 청바지 | `straight-leg jeans` | 추측(2003년 청바지 핏 자료 미확인. 2003년 큰 로고 청바지 유행은 [S25](https://www.hankookilbo.com/news/article/200301100084193889)) |
| 15 | `rubber boots` (은주·만석) | 색깔 있는 패션 레인부츠 | `plain dark rubber work boots` | 추측(1980년대 장화 색 미확인) |
| 16 | `white dress` (은주 무대) | 레이스·프릴 가운, 웨딩드레스풍 | `plain white cotton dress, long sleeves too long for her, no frills, no lace` | 대본 3화 S#17 + style_guide 7절 |

## 판정 건수 (표 1 기준)

표 1은 의상 라벨 55행, 머리·얼굴 16행, 단역 7행, 신규 지정 1행(최 계장 1950년대 회상)으로 모두 79행이다. 한 행에 판정이 두 개 붙은 경우('맞음(형태) / 색은 미확인' 등)는 앞의 판정으로 셌다.

| 범주 | 맞음 | 수정 권장 | 미확인 | 계 |
|---|---|---|---|---|
| 의상 라벨(55) | 7 | 8 | 40 | 55 |
| 머리·얼굴(16) | 2 | 0 | 14 | 16 |
| 단역(7) | 2 | 0 | 5 | 7 |
| 신규(1) | 0 | 1 | 0 | 1 |
| **합계** | **11** | **9** | **59** | **79** |

- 의상 '맞음' 7: 동민 큰 운동복, 선영 셔츠·카디건·플레어스커트, 미자 빨간 트레이닝 상의, 미자 빨간 트레이닝 위아래 2개(제일 좋은 옷·본선), 미자 2003 트레이닝복, 순례 몸뻬·앞치마(몸뻬 부분. 영문은 표 2 #17).
- 의상 '수정 권장' 8: 은주 학교옷(영문), 은주 흰 원피스(영문), 동민 여름 운동복(영문), 만석 야전상의(영문+본선 배정), 순례 본선 외출복, 봉구 본선, 석이 2개(영문).
- 머리 '맞음' 2: 선영 파마 단발, 순례 쪽진 머리. 순례의 핀은 표 2 #19에서 경미한 수정 권장.
- 판정은 '미확인'이지만 계절·연속성·영문 위험 때문에 표 2에 오른 항목이 있다: 곽 영감 앞치마(#11·#12), 최 계장 양복(#14), 선영 카디건(#13), 은주 여름옷·점퍼 배정(#5·#6), 동민 2-18·2-19·3-32(#8~#10), 태준 교복(#22), 객석(#23), 운동복 영문(#24).


## 적용 기록 (2026-10-09)

- 적용: 표 2 #1~#22, #24, #25(#9는 라벨 유지·영문에 흰 무릎 양말만, #10은 일정표 부분만). 표 3 보강 문구 중 운동복·교복·몸뻬·러닝셔츠·장갑·모자·까까머리(no fade)·청바지.
- 사용자 결정으로 바뀐 것: #19 비녀 승인(face와 6절 고정 문구). #18은 한복이 아니라 '자주색 블라우스 + 긴 치마'(2003 객석도 긴 치마). 은주 겨울 장갑은 2-14~2-16 자르지 않은 목장갑, 2-17(대본에서 영감이 손끝을 잘라 줌)부터 손끝 자른 목장갑.
- 미적용(고칠 수 있는 파일 밖): #23 객석 교복·사복(scene_presets), #26 섬사람 군중 얇은 작업복(scene_presets·style_guide 7-1), #27 3-34 동민 중복(scene_presets). `tools/char_prompts.py`의 2003 순례 문구('low bun')도 손대지 않음.
