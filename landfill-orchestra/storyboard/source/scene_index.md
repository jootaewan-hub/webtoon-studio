# 씬 색인 (G9 콘티·컷 사양 작성용, tools/scene_index.py로 생성)

컷 사양(cut_spec)의 `scene`·`set`·`spot`·`props`·`sound`는 아래 id를 그대로 쓴다. 소품은 상태 키가 있으면 그 씬에 맞는 상태 키를 쓴다.

## 1-1 갈대섬 작은 산 중턱 (새벽, 1987년 4월)
- 빛: 해 뜨기 전 회청색 확산광, 그림자 거의 없음. 끝 컷에서 화면 왼쪽(동쪽) 큰 산 너머로 첫 햇빛이 비침
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; extra:갈고리 아주머니=어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준); extra:섬사람들=어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준)
- 배경 `small_hill_slope` 작은 산 중턱 — 이 씬 카메라 자리: `slope_down_se`(중턱 단에서 남동쪽 아래로 롱숏: 큰 산 아래 하역, 둑길), `slope_wide`(비탈 전체 와이드(사람들이 일어서는 비탈)) / 그 밖: `slope_from_below_night`
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `island_end_south`(섬 쪽 끝에서 뭍 쪽으로(남향) 고정. 멀리 다가오는 사람) / 그 밖: `bank_side`, `middle_wide`, `low_shoes`
- 배경 `island_wide` 갈대섬 전경 — 이 씬 카메라 자리: 없음 / 그 밖: `high_north`
- 배경 `scrap_heap` 큰 산 아래 쇳더미 — 이 씬 카메라 자리: `from_small_hill`(작은 산 중턱에서 내려다본 롱숏(small_hill_slope의 slope_down_se)) / 그 밖: `heap_up`, `heap_pan`
- 소품: `scrap_sack`(고물 자루), `cotton_work_gloves`(목장갑), `rubber_boots`(고무장화(작업용)), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `iron_hook`(갈고리 아주머니의 갈고리), `soap_truck`(비누 공장 트럭), `ironworks_truck`(철공소 트럭)
- 소리 색 순간(이 컷들에만): 엔진 '쿨럭' #9DB7C9 — 은주 왼쪽 귀로 다가가는 컷(바람 빠지고 엔진만) / 쏟아지는 쇳소리가 낱낱으로 쪼개짐(깡·칭·짤랑·퉁·쨍) #9DB7C9 — 은주 옆얼굴 컷

## 1-2 갈대섬 큰 산 아래 쇳더미 (아침)
- 빛: 아침 낮은 해, 화면 왼쪽(동쪽)에서 비스듬히. 쇳더미에 짧은 금속 반사
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; mija=빨간 트레이닝 상의; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; extra:미자네 패거리 아이 둘=어두운 사복
- 배경 `scrap_heap` 큰 산 아래 쇳더미 — 이 씬 카메라 자리: `heap_up`(더미 아래에서 꼭대기(빨간 깃발)를 올려다봄(남향)), `heap_pan`(은주 시점, 더미를 천천히 훑는 팬) / 그 밖: `from_small_hill`
- 소품: `scrap_sack`(고물 자루), `cotton_work_gloves`(목장갑), `iron_rod`(은주의 짧은 쇠막대), `red_rag_flag`(미자의 빨간 헝겊 깃발), `copper_pipe_piece`(구리 파이프 토막(1화)), `nurungji`(누룽지), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `yellow_painted_iron`(노란 칠한 쇳덩이)
- 소리 색 순간(이 컷들에만): '깡'(노란 칠 쇳덩이) #9DB7C9 — 주변 소리 빠지고 그 소리만 / '통'(구리) #9DB7C9 — 둥글게 퍼졌다 길게 사그라지는 동심원, 은주 왼쪽 귀 클로즈업

## 1-3 곽 영감 고물상 (오후)
- 빛: 오후. 고물상 안은 그늘, 열린 문(둑길 쪽)에서 들어오는 측광. 선반의 바이올린 몸통만 먼지 없이 빛을 받음
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; kwak=톱밥 묻은 캔버스 앞치마·팔토시
- 배경 `junk_shop_in` 곽 영감 고물상 — 안 — 이 씬 카메라 자리: `east_wall_west`(동쪽 벽(선반) 쪽에서 서쪽을 보며 작업대 너머 영감 정면. 열린 전면은 화면 왼쪽(측광)), `shelf_pov`(작업대 옆 서쪽에서 작업대 너머 동쪽 벽 선반으로(은주 시선)), `exit_back`(안쪽에서 나가는 아이들 등 뒤(남향), 열린 전면 너머 마당) / 그 밖: `front_wide`, `bench_reverse`
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `yard_front`(마당(둑길 끝)에서 고물상 전면으로(북향) 외경) / 그 밖: `from_tent`, `village_south`
- 소품: `broken_violin_body__s1`(목 부러진 바이올린 몸통·선반 위), `rubber_boots`(고무장화(작업용)), `copper_pipe_piece`(구리 파이프 토막(1화)), `hanging_scale`(걸이 저울(고물상)), `workbench`(곽 영감의 작업대(서랍 포함)), `sawdust`(톱밥), `scrap_money`(고물값 지폐·동전), `tin_roof`(고물상 함석지붕), `kwak_pencil`(곽 영감이 귀에 꽂은 연필), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `bottle_caps`(동민의 병뚜껑 한 주먹), `polishing_cloth`(곽 영감의 부드러운 천)
- 소리 색 순간(이 컷들에만): 나무 몸통 '똑'과 그 안의 '오오' #9DB7C9 — 은주 왼쪽 귀로, 주변 소리 빠짐

## 1-4 은주네 판잣집, 부엌 겸 방 (저녁)
- 빛: 외경: 남색 박명, 판잣집 창 몇 개에 노란 불. 안: 백열전구 하나와 석유곤로 불빛, 문틈 연탄 연기
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; manseok=낡은 야전상의·목수건·고무장화
- 배경 `shack_main` 은주네 판잣집 — 부엌 겸 방 — 이 씬 카메라 자리: `door_wide`(현관문 안에서 방 안쪽으로(북향). 작은 창·곤로 왼쪽, 합판 벽·쪽방 문 오른쪽 안), `table_front`(방 안쪽(북쪽)에서 밥상 정면, 뒤로 현관문(남향). 세 사람 밥상 정면), `section`(합판 벽을 가운데 두고 두 칸을 단면처럼 한 화면(남쪽 벽을 걷어낸 단면, 북향). 왼쪽 부엌 겸 방, 오른쪽 쪽방), `door_close`(현관문 안쪽 문고리·목수건·못의 손전등 가까이)
- 배경 `shack_village` 판잣집 동네 외경 — 이 씬 카메라 자리: `alley_west`(골목 안에서 서쪽으로: 오른쪽에 은주네 집 현관) / 그 밖: `roofs_to_entrance`
- 소품: `kerosene_stove`(석유곤로와 냄비), `low_table`(밥상(접이식 낮은 상)), `bowls_spoons`(밥그릇·국그릇·숟가락·젓가락), `neck_towel`(만석의 목수건), `plywood_wall`(합판 벽(판잣집 칸막이)), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `shack_door`(판잣집 문과 문고리), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `kimchi_jjigae`(김치찌개), `tool_sack`(만석의 공구 자루)
- 소리 색 순간(이 컷들에만): 문밖 긴 한숨 '후우―' #9DB7C9 — 은주 왼쪽 귀로, 찌개 소리 빠짐

## 1-5 은주네 판잣집, 쪽방 (밤)
- 빛: 쪽방 백열전구 하나(위에서), 소리굽쇠에 반짝임. 불 끈 뒤 거의 어둠, 남색
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: `top_down`(위에서 내려다보며: 이불 위 은주와 무릎, 머리맡 선반), `door_south`(쪽방 문에서 방 끝 작은 창 쪽으로(남향). 합판 벽 오른쪽, 선반 왼쪽 안), `wall_close`(합판 벽과 손가락 마디 극접사(톡톡)), `section`(두 칸 단면(shack_main의 section과 같은 그림)) / 그 밖: `window_from_mat`
- 소품: `tuning_fork_necklace__s1_worn`(은색 소리굽쇠 목걸이·착용 — 꺼내 쓸 때(옷 속에서 꺼냄)), `mother_radio__s1_broken`(엄마의 고장 난 트랜지스터라디오·고장 — 은주가 고쳐 보는 라디오), `mother_radio__s1b_open_back`(엄마의 고장 난 트랜지스터라디오·뒤판을 연 모습(1-5)), `scrap_money`(고물값 지폐·동전), `blanket`(이불), `plywood_wall`(합판 벽(판잣집 칸막이)), `bulb`(백열전구), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `dongmin_tracksuit`(동민의 물려받은 큰 운동복)
- 소리 색 순간(이 컷들에만): 소리굽쇠 '웅―' #E9EEF5 — 주변 소리 모두 빠짐, 은주 눈 감음 / 라디오 허밍 '음―' #B9A7D9 — 지지직 사이 아주 잠깐, 은주 숨 멈춘 정면 고정 컷

## 1-6 강변교회 지하 공부방 (토요일 저녁)
- 빛: 지하 교실, 천장 백열등 세 개가 노랗게 흔들림(대본). 흔들리는 그림자
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; extra:섬 아이들 몇=어두운 사복
- 배경 `night_school` 강변교회 지하 공부방 — 이 씬 카메라 자리: `bulb_down`(백열등에서 내려와 교실 전체로), `stairs_up`(계단 아래에서 올려다봄(사탕이 화면 쪽으로 쏟아짐)), `across_room`(교실을 사이에 두고 칠판 앞 선영과 뒷줄 은주 투샷(옆에서))
- 소품: `empty_violin_case__s1_spilled`(선영의 빈 바이올린 케이스·계단에서 뒤집혀 열림(1-6)), `seonyoung_shoes`(선영의 구두), `bulb`(백열전구), `sheet_music`(선영의 악보), `candy`(알록달록 사탕), `bus_token`(버스 토큰), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `chalk`(분필(끝이 쪼개진)), `chalkboard`(공부방 칠판), `dictation_notebook`(동민의 받아쓰기 공책)
- 소리 색 순간(이 컷들에만): 케이스 닫는 '텅' #9DB7C9 — 주변 소리 빠지고 그 소리만

## 1-7 갈대섬 둑길 끝, 섬 어귀 (오후, 다음 주 토요일)
- 빛: 비 갠 뒤 엷은 구름 사이 오후 빛, 화면 오른쪽(서쪽)에서. 물웅덩이 반사
- 인물·의상: seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; sunrye=몸뻬 바지·꽃무늬 앞치마
- 배경 `soup_tent_front` 국밥집 천막 — 앞 — 이 씬 카메라 자리: 없음 / 그 밖: `yard_north`, `front_east`, `low_mud`
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `island_end_south`(섬 쪽 끝에서 뭍 쪽으로(남향) 고정. 멀리 다가오는 사람), `bank_side`(둑 비탈에 줄지어 앉은 아이들 너머 둑길(옆에서, 동향 또는 서향)) / 그 밖: `middle_wide`, `low_shoes`
- 소품: `empty_violin_case__s2_carried`(선영의 빈 바이올린 케이스·들고 다니는 모습(닫힘)), `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `seonyoung_shoes`(선영의 구두), `nurungji`(누룽지), `soup_tent`(국밥집 천막), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트)

## 1-8 국밥집 천막 안 (오후, 연속)
- 빛: 천막 천을 거친 부드러운 확산광, 솥 김에 흐림. 천막 옆 고물상은 바깥 빛
- 인물·의상: seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; mija=빨간 트레이닝 상의; sunrye=몸뻬 바지·꽃무늬 앞치마; kwak=톱밥 묻은 캔버스 앞치마·팔토시; extra:미자네 패거리 아이 둘=어두운 사복
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `from_tent`(천막 동쪽 옆자락 안에서 고물상 열린 전면을 비스듬히(북동향) — 작업대의 영감 등) / 그 밖: `yard_front`, `village_south`
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `entrance_wide`(앞자락(남)에서 안쪽으로 와이드(북향). 국솥 정면 안쪽, 기둥 가운데, 걷힌 옆자락 오른쪽), `side_to_shop`(동쪽 평상 끝에서 걷힌 옆자락 너머 고물상으로(동향). 아이들 뒤통수 너머 영감의 등) / 그 밖: `pot_reverse`, `band_front`, `bench_end`
- 소품: `empty_violin_case__s2_carried`(선영의 빈 바이올린 케이스·들고 다니는 모습(닫힘)), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `soup_pot__s1`(국솥(국밥집 무쇠 솥)·김이 오르는 솥), `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `workbench`(곽 영감의 작업대(서랍 포함)), `candy`(알록달록 사탕), `pyeongsang`(평상), `sandpaper`(사포), `soup_tent`(국밥집 천막), `glasses_seonyoung`(선영의 동그란 금테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트)
- 소리 색 순간(이 컷들에만): 사포질 '쓱, 쓱'이 끊긴 빈자리 #9DB7C9 — 은주 왼쪽 귀로, 웃음 낮아짐

## 1-9 곽 영감 고물상 앞 (오후, 연속)
- 빛: 고물상 앞 오후 측광(서쪽, 화면 오른쪽), 함석지붕 아래 그늘
- 인물·의상: seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; kwak=톱밥 묻은 캔버스 앞치마·팔토시; eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `junk_shop_in` 곽 영감 고물상 — 안 — 이 씬 카메라 자리: `bench_reverse`(작업대 안쪽 끝(북)에서 열린 전면 쪽으로(남향). 작업대에 앉은 영감의 왼쪽 옆얼굴, 그 너머 문간이 밝게(역광), 문간에 선 사람) / 그 밖: `front_wide`, `east_wall_west`, `shelf_pov`, `exit_back`
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `yard_front`(마당(둑길 끝)에서 고물상 전면으로(북향) 외경) / 그 밖: `from_tent`, `village_south`
- 배경 `soup_tent_front` 국밥집 천막 — 앞 — 이 씬 카메라 자리: `yard_north`(마당에서 천막 앞으로 와이드(북향). 고물상은 오른쪽) / 그 밖: `front_east`, `low_mud`
- 소품: `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `sandpaper`(사포), `tin_roof`(고물상 함석지붕), `glasses_seonyoung`(선영의 동그란 금테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `kwak_wood_piece`(곽 영감이 사포질하는 나뭇조각), `ladder_attic`(고물상 사다리와 다락)
- 소리 색 순간(이 컷들에만): 느려진 사포 소리 #9DB7C9 — 은주 왼쪽 귀로

## 1-10 은주네 판잣집, 쪽방 (밤)
- 빛: 본 장면: 쪽방 어둠, 창으로 희미한 남색. 1: 고물상 함석지붕 틈으로 새는 노란 작업등. 2: 쪽방 같은 어둠. 3: 판잣집 지붕들 너머 고물상 불빛 하나
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `village_south`(마을 쪽(북)에서 고물상 지붕 너머 둑길 쪽(남향) — 아침 해가 지붕 왼쪽(동)에서) / 그 밖: `yard_front`, `from_tent`
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: `window_from_mat`(이불에 누운 높이에서 작은 창(창틀 안 먼 불빛 둘)) / 그 밖: `top_down`, `door_south`, `wall_close`, `section`
- 배경 `shack_village` 판잣집 동네 외경 — 이 씬 카메라 자리: `roofs_to_entrance`(은주네 집 근처에서 지붕들 너머 남동쪽 섬 어귀(고물상 불빛 하나)) / 그 밖: `alley_west`
- 소품: `mother_radio__s1_broken`(엄마의 고장 난 트랜지스터라디오·고장 — 은주가 고쳐 보는 라디오), `blanket`(이불), `tin_roof`(고물상 함석지붕), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼)
- 소리 색 순간(이 컷들에만): 톱질 '쓱싹'·망치 '똑' #9DB7C9 — 은주 왼쪽 귀로

## 1-11 작은 산 꼭대기 (저녁, 나흘째)
- 빛: 해 질 녘 역광, 화면 오른쪽(서쪽) 강 너머 낮은 해, 긴 그림자. 쓰레기 산 전체가 금빛
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; kwak=톱밥 묻은 캔버스 앞치마·팔토시; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; mija=빨간 트레이닝 상의; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; dongmin=물려받은 큰 운동복; extra:미자네 패거리=어두운 사복; extra:비탈의 섬사람들·집하장 아저씨=어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준)
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: `top_south`(꼭대기 가운데에서 남쪽(판자·마을·둑길·뭍)으로 와이드), `slope_up`(남쪽 비탈 아래에서 꼭대기 가장자리로 올려다봄(북향). 오르는 사람 등 너머 아이들 얼굴) / 그 밖: `board_close`, `sky_low`
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `tuning_fork_necklace__s1_worn`(은색 소리굽쇠 목걸이·착용 — 꺼내 쓸 때(옷 속에서 꺼냄)), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `cotton_work_gloves`(목장갑), `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `wrap_cloth`(동그리를 싼 천), `candy`(알록달록 사탕), `nurungji`(누룽지), `glasses_seonyoung`(선영의 동그란 금테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `white_vinyl`(쓰레기 산의 흰 비닐 조각), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트)
- 소리 색 순간(이 컷들에만): 조율: 줄 소리 #F5C04A(옅게) + 소리굽쇠 '웅―' #E9EEF5 — 떨리다 하나로 포개지는 순간 / 끼익 밑에 숨은 동그란 소리 하나 #F5C04A — 한 점 / 동그리 첫 소리 #F5C04A — 두 번째 활부터 활을 내릴 때까지(바람·비닐·웃음·쇳소리가 한 겹씩 빠짐)

## 1-12 곽 영감 고물상 (오후, 다음 날부터 며칠)
- 빛: 오후, 고물상 안 그늘과 열린 문의 측광. 동민이 X선 필름을 해 쪽으로 드는 역광 컷. 바깥 와이드는 뿌연 베이지 하늘
- 인물·의상: kwak=톱밥 묻은 캔버스 앞치마·팔토시; eunju=큰 남색 점퍼·해진 바지·목장갑; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; dongmin=물려받은 큰 운동복; mija=빨간 트레이닝 상의; sunrye=몸뻬 바지·꽃무늬 앞치마
- 배경 `junk_shop_in` 곽 영감 고물상 — 안 — 이 씬 카메라 자리: `front_wide`(마당에서 열린 전면 안쪽으로 와이드(북향). 작업대 오른쪽, 공방 문 뒤 왼쪽) / 그 밖: `bench_reverse`, `east_wall_west`, `shelf_pov`, `exit_back`
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `yard_front`(마당(둑길 끝)에서 고물상 전면으로(북향) 외경) / 그 밖: `from_tent`, `village_south`
- 소품: `ttungbo__s1_making`(뚱보(기름통 첼로)·제작 중(1-12)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s1_leaking`(꽥꽥이(배수관 트럼펫)·처음(바람 샘, 1-12 수리 전)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s1_film_drying`(뼈다귀 북(X선 필름 북)·제작 — 씻어 말리는 X선 필름(1-12)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `drumstick_spoons`(북채(나무 숟가락 두 개)), `workbench`(곽 영감의 작업대(서랍 포함)), `nurungji`(누룽지), `tin_roof`(고물상 함석지붕), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `xray_film_line`(X선 필름 빨랫줄과 비눗물 대야), `workbench_screws`(작업대 위 나사못)
- 소리 색 순간(이 컷들에만): 뚱보 '부우웅'(두 번째, 둥글어진 소리) #E8944A — 은주 왼쪽 귀로 / 꽥꽥이 이음매 왼쪽 새는 바람 '쉬이' #4FB3A9 — 은주 왼쪽 귀로, 동민 웃음 빠짐

## 1-13 몽타주 — 고물상과 작은 산 (4월 말)
- 빛: 1: 아침, 고물상 함석지붕 위로 해 뜸(화면 왼쪽 동쪽). 2: 저녁, 작은 산 꼭대기 해 질 녘 역광(오른쪽 서쪽). 3: 고물상 안 벽, 낮 그늘
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `junk_shop_in` 곽 영감 고물상 — 안 — 이 씬 카메라 자리: 없음 / 그 밖: `front_wide`, `bench_reverse`, `east_wall_west`, `shelf_pov`, `exit_back`
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `village_south`(마을 쪽(북)에서 고물상 지붕 너머 둑길 쪽(남향) — 아침 해가 지붕 왼쪽(동)에서) / 그 밖: `yard_front`, `from_tent`
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: 없음 / 그 밖: `top_south`, `slope_up`, `board_close`, `sky_low`
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `tin_roof`(고물상 함석지붕), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `calendar_junkshop`(고물상 벽 달력)
- 소리 색 순간(이 컷들에만): 2: M: 아직 서툰 동그리 #F5C04A — 얇고 끊기는 빛 띠

## 1-14 국밥집 천막 (오후, 5월 첫 토요일)
- 빛: 오후, 천막 천을 거친 확산광. 금빛 테두리 종이가 천막 그늘 속에서 반짝
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; mija=빨간 트레이닝 상의; dongmin=물려받은 큰 운동복; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; kwak=톱밥 묻은 캔버스 앞치마·팔토시; sunrye=몸뻬 바지·꽃무늬 앞치마; extra:국밥 먹는 아저씨들=어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준)
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `entrance_wide`(앞자락(남)에서 안쪽으로 와이드(북향). 국솥 정면 안쪽, 기둥 가운데, 걷힌 옆자락 오른쪽) / 그 밖: `pot_reverse`, `side_to_shop`, `band_front`, `bench_end`
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `soup_pot__s1`(국솥(국밥집 무쇠 솥)·김이 오르는 솥), `contest_poster__s1_rolled`(전국 청소년 합주제 공고(금빛 테두리 종이)·둘둘 말린 종이를 폄(1-14)), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `pyeongsang`(평상), `soup_tent`(국밥집 천막), `glasses_seonyoung`(선영의 동그란 금테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `gukbap`(국밥(뚝배기)), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트)

## 1-15 섬 어귀 게시판 (저녁)
- 빛: 저녁, 해 질 무렵 낮은 빛이 화면 오른쪽(서쪽)에서, 금빛 테두리 종이에 반사
- 인물·의상: seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; dongmin=물려받은 큰 운동복
- 배경 `notice_board` 섬 어귀 게시판 — 이 씬 카메라 자리: `board_front`(마당에서 게시판 정면(남향). 오른쪽으로 둑길이 뭍까지), `thumbtack_close`(압정 머리·종이 귀퉁이 극접사) / 그 밖: `over_shoulder`, `road_north`
- 소품: `contest_poster__s2_pinned`(전국 청소년 합주제 공고(금빛 테두리 종이)·게시판에 압정 네 개), `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `notice_board`(섬 어귀 나무 게시판), `thumbtacks`(압정과 압정 통), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트)

## 1-16 둑길과 섬 어귀 게시판 (아침, 이튿날)
- 빛: 이른 아침 낮은 해 화면 왼쪽(동쪽), 차갑고 맑은 빛, 이슬 반짝임
- 인물·의상: choi=회색 양복·넥타이·서류 봉투
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `low_shoes`(진흙 바퀴 자국 위 구두·장화(낮게)) / 그 밖: `island_end_south`, `bank_side`, `middle_wide`
- 배경 `notice_board` 섬 어귀 게시판 — 이 씬 카메라 자리: `board_front`(마당에서 게시판 정면(남향). 오른쪽으로 둑길이 뭍까지), `thumbtack_close`(압정 머리·종이 귀퉁이 극접사) / 그 밖: `over_shoulder`, `road_north`
- 소품: `choi_handkerchief__s1_dry`(최 계장의 손수건·마른 손수건), `contest_poster__s2_pinned`(전국 청소년 합주제 공고(금빛 테두리 종이)·게시판에 압정 네 개), `clearance_notice_1987__s1`(갈대섬 정리 예정 알림(회색 갱지)·게시판에 붙은 알림), `notice_board`(섬 어귀 나무 게시판), `thumbtacks`(압정과 압정 통), `choi_envelope`(최 계장의 누런 서류 봉투), `choi_shoes`(최 계장의 반들반들한 구두), `choi_gray_suit`(최 계장의 회색 양복)

## 1-17 섬 어귀 게시판 (아침, 조금 뒤)
- 빛: 아침 빛 화면 왼쪽(동쪽), 둑길 바퀴 자국 그늘. 두 종이가 같은 빛에 함께 떨림
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `small_hill_slope` 작은 산 중턱 — 이 씬 카메라 자리: 없음 / 그 밖: `slope_down_se`, `slope_wide`, `slope_from_below_night`
- 배경 `notice_board` 섬 어귀 게시판 — 이 씬 카메라 자리: `board_front`(마당에서 게시판 정면(남향). 오른쪽으로 둑길이 뭍까지), `over_shoulder`(은주 어깨 너머 게시판, 종이 두 장 나란히(남향)), `road_north`(둑길에서 섬 쪽(북향): 걸어오는 은주, 그 뒤 고물상 함석지붕) / 그 밖: `thumbtack_close`
- 소품: `contest_poster__s2_pinned`(전국 청소년 합주제 공고(금빛 테두리 종이)·게시판에 압정 네 개), `clearance_notice_1987__s1`(갈대섬 정리 예정 알림(회색 갱지)·게시판에 붙은 알림), `scrap_sack`(고물 자루), `cotton_work_gloves`(목장갑), `tin_roof`(고물상 함석지붕), `notice_board`(섬 어귀 나무 게시판), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼)
- 소리 색 순간(이 컷들에만): 사락(금빛 공고)과 바스락(회색 공문) 둘 다 #9DB7C9, 같은 세기로 번갈아·겹쳐서 — 어느 쪽도 키우지 않음

## 2-1 국밥집 천막 (낮, 1987년 9월~10월 주말들)
- 빛: 본 장면·3·4·6·7·9: 천막 천 확산광, 오후. 1: 토요일 아침 둑길, 왼쪽(동쪽) 낮은 해. 2: 뭍 골목, 해가 아직 높은 낮. 5: 섬 어귀 오후. 8: 10월 오후, 서늘하고 맑은 빛. 10·11: 쓰레기 산 낮
- 인물·의상: dongmin=물려받은 큰 운동복; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; eunju=큰 남색 점퍼·해진 바지·목장갑; mija=빨간 트레이닝 상의; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; manseok=낡은 야전상의·목수건·고무장화; kwak=톱밥 묻은 캔버스 앞치마·팔토시; sunrye=몸뻬 바지·꽃무늬 앞치마; extra:섬 아저씨들=어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준)
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `band_front`(서쪽 평상에서 가운데 바닥의 연주자들 정면(동향). 뒤로 동쪽 평상과 옆자락) / 그 밖: `entrance_wide`, `pot_reverse`, `side_to_shop`, `bench_end`
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: 없음 / 그 밖: `top_south`, `slope_up`, `board_close`, `sky_low`
- 배경 `small_hill_slope` 작은 산 중턱 — 이 씬 카메라 자리: `slope_wide`(비탈 전체 와이드(사람들이 일어서는 비탈)) / 그 밖: `slope_down_se`, `slope_from_below_night`
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `low_shoes`(진흙 바퀴 자국 위 구두·장화(낮게)) / 그 밖: `island_end_south`, `bank_side`, `middle_wide`
- 배경 `island_wide` 갈대섬 전경 — 이 씬 카메라 자리: `high_north`(뭍 쪽 하늘에서 섬 전체를 북향으로 내려다보는 높은 와이드)
- 배경 `mainland_alley` 뭍의 골목 — 이 씬 카메라 자리: `lane_along`(골목을 따라 리어카를 끄는 만석)
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s2_soup`(지휘봉(숟가락 자루 막대)·국솥에 빠졌다 건짐(2-1)), `empty_violin_case__s2_carried`(선영의 빈 바이올린 케이스·들고 다니는 모습(닫힘)), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `soup_pot__s1`(국솥(국밥집 무쇠 솥)·김이 오르는 솥), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `drumstick_spoons`(북채(나무 숟가락 두 개)), `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `iron_rod`(은주의 짧은 쇠막대), `handcart`(리어카), `nurungji`(누룽지), `pyeongsang`(평상), `soup_tent`(국밥집 천막), `piano_wire`(피아노 쇠줄 다발), `glasses_seonyoung`(선영의 동그란 금테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `calendar_tent`(천막 기둥 달력), `broken_piano`(부서진 피아노), `dish_towel`(순례 할머니의 행주)
- 소리 색 순간(이 컷들에만): 은주 귀로: 꽥꽥이 소리 밑에 깔린 가는 동그리 소리 #F5C04A — 꽥꽥이 #4FB3A9는 채도 낮춰 위에 덮이게

## 2-2 국밥집 천막 (오후, 1987년 10월 둘째 토요일)
- 빛: 늦은 오후, 천막 기둥에 매단 전구 하나가 흔들리며 따뜻한 빛, 천막 밖 남은 낮빛
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; mija=빨간 트레이닝 상의; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `band_front`(서쪽 평상에서 가운데 바닥의 연주자들 정면(동향). 뒤로 동쪽 평상과 옆자락) / 그 밖: `entrance_wide`, `pot_reverse`, `side_to_shop`, `bench_end`
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `big_black_boots`(선영이 빌린 검정 고무장화(큰 치수)), `bulb`(백열전구), `pyeongsang`(평상), `soup_tent`(국밥집 천막), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트)

## 2-3 시내버스 안 (낮, 1987년 10월 말)
- 빛: 한낮, 버스 창으로 들어오는 밝은 측광, 흔들리는 창틀 그림자
- 인물·의상: seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; mija=빨간 트레이닝 상의; extra:승객들=1980년대 사복
- 배경 `city_bus` 시내버스 안 — 이 씬 카메라 자리: `aisle_back`(통로 따라 뒤로 미끄러지며(맨 뒷자리 아이들))
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `contest_leaflet__s1`(합주제 참가 설명회 안내문(전단)·안내문), `scrap_sack`(고물 자루), `bus_token`(버스 토큰), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `city_bus`(시내버스(내부·토큰함))

## 2-4 한빛문화회관 연습실 (낮)
- 빛: 흰 형광등(윙―)의 평평한 빛 + 창으로 드는 햇볕 띠
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; mija=빨간 트레이닝 상의; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; taejun=사립학교 교복(감색 재킷·넥타이); extra:다솜중 단원·다른 학교 아이들·진행 간사=교복(감색 재킷 등)
- 배경 `hanbit_rehearsal` 한빛문화회관 연습실 — 이 씬 카메라 자리: `room_wide`(뒷문 쪽에서 앞으로 와이드(창 왼쪽)), `last_rows`(맨 뒷줄과 바로 앞줄 사이(은주·태준 교차))
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s1_worn`(은색 소리굽쇠 목걸이·착용 — 꺼내 쓸 때(옷 속에서 꺼냄)), `taejun_violin__s1`(태준의 바이올린·변화 없음), `contest_leaflet__s1`(합주제 참가 설명회 안내문(전단)·안내문), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `scrap_sack`(고물 자루), `taejun_case`(태준의 고급 바이올린 케이스), `olympic_poster`(올림픽 표어 포스터(표어만)), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `taejun_uniform`(태준의 다솜중 교복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `taejun_rag`(태준의 송진 닦는 헝겊)
- 소리 색 순간(이 컷들에만): M: 비발디 '여름' 3악장 #5B8DEF — 은주 귀로, 한 덩어리 합주가 줄 하나하나의 빛 띠로 갈라짐 / 소리굽쇠 '웅―' #E9EEF5 — 조율 / 동그리 두 줄 울림 #F5C04A — 태준 쪽에서, 웃음 가라앉고 두 줄 울림만 / 태준의 라 '팅' #5B8DEF — 은주 귀로, 소리굽쇠 '웅―' #E9EEF5 잔향과 겹쳐 아주 가늘게 어긋나 일렁임

## 2-5 갈대섬 둑길 (오후, 1987년 11월 초)
- 빛: 오후, 차가운 맑은 빛 화면 오른쪽(서쪽)
- 인물·의상: choi=회색 양복·넥타이·서류 봉투
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `island_end_south`(섬 쪽 끝에서 뭍 쪽으로(남향) 고정. 멀리 다가오는 사람), `low_shoes`(진흙 바퀴 자국 위 구두·장화(낮게)) / 그 밖: `bank_side`, `middle_wide`
- 소품: `choi_envelope`(최 계장의 누런 서류 봉투), `choi_shoes`(최 계장의 반들반들한 구두), `glasses_choi`(최 계장의 검은 뿔테 안경), `choi_gray_suit`(최 계장의 회색 양복), `survey_form`(갈대섬 가구 조사표)

## 2-6 국밥집 천막 앞 (오후)
- 빛: 오후 맑은 빛 화면 오른쪽(서쪽). 회색 톤 속에 함석지붕 위 맑은 하늘 한 줄
- 인물·의상: choi=회색 양복·넥타이·서류 봉투; deoksu=늘어난 흰 러닝셔츠 위 체크 남방
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `from_tent`(천막 동쪽 옆자락 안에서 고물상 열린 전면을 비스듬히(북동향) — 작업대의 영감 등) / 그 밖: `yard_front`, `village_south`
- 배경 `soup_tent_front` 국밥집 천막 — 앞 — 이 씬 카메라 자리: `front_east`(천막 앞에서 동쪽 고물상 함석지붕을 올려다봄(동향). 해는 등 뒤 오른쪽), `low_mud`(진흙 위 구두에서 틸트 업(낮게)) / 그 밖: `yard_north`
- 소품: `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `choi_handkerchief__s1_dry`(최 계장의 손수건·마른 손수건), `soup_tent`(국밥집 천막), `tin_roof`(고물상 함석지붕), `choi_shoes`(최 계장의 반들반들한 구두), `glasses_choi`(최 계장의 검은 뿔테 안경), `deoksu_check_shirt`(덕수의 체크 남방), `choi_gray_suit`(최 계장의 회색 양복)
- 소리 색 순간(이 컷들에만): 뚱보 '부우우우웅―' #E8944A — 진흙 물웅덩이 잔물결에서 구두·발목·무릎으로, 바람 소리 빠짐

## 2-7 갈대섬 둑길 한가운데 (오후, 이어서)
- 빛: 오후 기우는 빛 화면 오른쪽(서쪽), 둑길 위 긴 그림자
- 인물·의상: choi=회색 양복·넥타이·서류 봉투
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `middle_wide`(둑길 한가운데 작아지는 사람, 와이드(남향)) / 그 밖: `island_end_south`, `bank_side`, `low_shoes`
- 소품: `choi_handkerchief__s1_dry`(최 계장의 손수건·마른 손수건), `ballpoint_pen`(볼펜), `glasses_choi`(최 계장의 검은 뿔테 안경), `choi_gray_suit`(최 계장의 회색 양복), `choi_memo`(최 계장의 수첩)

## 2-8 만복전당포 (아침, 1987년 11월 중순)
- 빛: 바깥: 서리 낀 아침 차가운 빛. 안: 누렇게 깜빡이는 형광등(치익)
- 인물·의상: seonyoung=베이지 더플코트·목도리(늦가을~겨울); manseok=낡은 야전상의·목수건·고무장화; extra:전당포 주인=어두운 조끼·돋보기(근거 없음, 제안)
- 배경 `pawnshop` 만복전당포 — 이 씬 카메라 자리: `door_in`(문 안에서 계산대 쪽으로(진열장 왼쪽)), `counter_reverse`(계산대 뒤 주인 자리에서 문 쪽으로(문 종, 들어오는 사람)), `counter_top`(계산대 위 부감(케이스 안, 전당표, 동전))
- 배경 `market_alley` 시장 골목 — 이 씬 카메라 자리: `sign_down`(전당포 간판에서 문 앞으로 내려옴) / 그 밖: `mouth_in`, `radio_close`
- 소품: `empty_violin_case__s3_pawnshop`(선영의 빈 바이올린 케이스·전당포 진열장 위 — 전당표를 악보 사이에), `pawn_ticket_manseok__s1`(만석의 전당표·닳은 전당표), `rubber_boots`(고무장화(작업용)), `scrap_money`(고물값 지폐·동전), `neck_towel`(만석의 목수건), `sheet_music`(선영의 악보), `candy`(알록달록 사탕), `door_bell`(전당포 문 위의 종), `abacus`(주판), `glasses_seonyoung`(선영의 동그란 금테 안경), `work_cap_manseok`(만석의 국방색 작업모), `manseok_field_jacket`(만석의 낡은 야전상의), `pawnshop_showcase`(전당포 유리 진열장과 계산대), `pawnshop_sign`(만복전당포 간판), `pawn_ticket_seonyoung`(선영의 전당표), `pawn_stamp`(전당포 도장)

## 2-9 시장 골목 (아침, 이어서)
- 빛: 아침 차가운 빛, 골목 그늘에 서리, 입김
- 인물·의상: seonyoung=베이지 더플코트·목도리(늦가을~겨울); manseok=낡은 야전상의·목수건·고무장화
- 배경 `market_alley` 시장 골목 — 이 씬 카메라 자리: `mouth_in`(골목 어귀에서 안쪽 끝 전당포 쪽으로), `radio_close`(전파사 진열대 라디오 스피커 극접사) / 그 밖: `sign_down`
- 소품: `empty_violin_case__s2_carried`(선영의 빈 바이올린 케이스·들고 다니는 모습(닫힘)), `handcart`(리어카), `glasses_seonyoung`(선영의 동그란 금테 안경), `work_cap_manseok`(만석의 국방색 작업모), `manseok_field_jacket`(만석의 낡은 야전상의), `electronics_shop_radio`(전파사 진열대 라디오)
- 소리 색 순간(이 컷들에만): M: 전파사 라디오 노래의 관악기 #9C4A6B(만석의 클라리넷 색) — 라디오 스피커 극접사에서 뻗어 나오고, 만석이 멀어질수록 작아짐

## 2-10 국밥집 천막 (낮, 1987년 11월 말, 비)
- 빛: 회색 한낮, 빗줄기, 젖은 천막 천을 거친 탁한 확산광. 그림자 약함
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; dongmin=물려받은 큰 운동복; mija=빨간 트레이닝 상의; manseok=낡은 야전상의·목수건·고무장화; sunrye=몸뻬 바지·꽃무늬 앞치마
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `pot_reverse`(국솥 쪽에서 앞자락 쪽으로(남향). 문간에 선 사람, 빈 입구), `band_front`(서쪽 평상에서 가운데 바닥의 연주자들 정면(동향). 뒤로 동쪽 평상과 옆자락) / 그 밖: `entrance_wide`, `side_to_shop`, `bench_end`
- 배경 `soup_tent_front` 국밥집 천막 — 앞 — 이 씬 카메라 자리: `yard_north`(마당에서 천막 앞으로 와이드(북향). 고물상은 오른쪽) / 그 밖: `front_east`, `low_mud`
- 배경 `soup_tent_back` 국밥집 천막 — 뒤 쓰레기 더미 — 이 씬 카메라 자리: `rear_flap`(천막 안 국솥 옆 뒷자락 너머 빗속의 더미(북향, 2-10)) / 그 밖: `path_south`, `far_window`
- 소품: `dongguri__s1_first`(동그리(깡통 바이올린 1호)·처음(곽 영감이 만든 그대로)), `dongguri__s2_thrown`(동그리(깡통 바이올린 1호)·던져짐 — 포크 줄받침 꺾임), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `drumstick_spoons`(북채(나무 숟가락 두 개)), `rubber_boots`(고무장화(작업용)), `neck_towel`(만석의 목수건), `handcart`(리어카), `pyeongsang`(평상), `soup_tent`(국밥집 천막), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `trash_mound_wet`(천막 뒤 젖은 쓰레기 더미)
- 소리 색 순간(이 컷들에만): M: 동그리 「도라지 타령」 #F5C04A — 빗소리 위, 바퀴 소리가 멎을 때 끊김 / 멀리 리어카 바퀴 '끼익, 덜컹' #9DB7C9 — 은주 왼쪽 귀로 / 포크 줄받침 꺾이는 '딱' #F5C04A — 동그리 금빛이 꺼져 가는 작은 한 점, 은주 왼쪽 귀 극접사, 빗소리 빠짐

## 2-11 은주네 판잣집, 쪽방 (밤, 같은 날)
- 빛: 쪽방 어둠, 작은 창 밖 멀리 손전등 불빛 둘(하나는 움직이고 하나는 멈춤)
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `soup_tent_back` 국밥집 천막 — 뒤 쓰레기 더미 — 이 씬 카메라 자리: `far_window`(은주네 쪽방 창에서 본 먼 더미 위 불빛 둘(롱, 남동향)) / 그 밖: `path_south`, `rear_flap`
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: `top_down`(위에서 내려다보며: 이불 위 은주와 무릎, 머리맡 선반), `window_from_mat`(이불에 누운 높이에서 작은 창(창틀 안 먼 불빛 둘)), `wall_close`(합판 벽과 손가락 마디 극접사(톡톡)) / 그 밖: `door_south`, `section`
- 소품: `mother_radio__s1_broken`(엄마의 고장 난 트랜지스터라디오·고장 — 은주가 고쳐 보는 라디오), `radio_box__s1_closed`(라디오 상자(나무 상자)·선반 위 닫힌 상자), `blanket`(이불), `plywood_wall`(합판 벽(판잣집 칸막이)), `flashlight`(손전등), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼)
- 소리 색 순간(이 컷들에만): 멀리 헤집는 소리·깡통 짤그랑 #9DB7C9 — 은주 왼쪽 귀로

## 2-12 국밥집 천막 뒤 쓰레기 더미 (밤, 같은 시각)
- 빛: 어둠, 손전등 불빛 둘(덕수 것은 움직이고 어른 것은 아이들 발치를 꼼짝 않고 비춤)
- 인물·의상: mija=빨간 트레이닝 상의; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; kwak=톱밥 묻은 캔버스 앞치마·팔토시
- 배경 `soup_tent_back` 국밥집 천막 — 뒤 쓰레기 더미 — 이 씬 카메라 자리: `path_south`(마을 흙길에서 천막 뒤와 더미(남향)) / 그 밖: `rear_flap`, `far_window`
- 소품: `cotton_work_gloves`(목장갑), `rubber_boots`(고무장화(작업용)), `flashlight`(손전등), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `trash_mound_wet`(천막 뒤 젖은 쓰레기 더미), `mija_stick`(미자의 막대기)

## 2-13 곽 영감 고물상 (낮, 이튿날 오후)
- 빛: 오후, 고물상 안 그늘, 문간 측광. 작업대 위 닦인 동그리에 반짝임
- 인물·의상: mija=빨간 트레이닝 상의; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; eunju=큰 남색 점퍼·해진 바지·목장갑; kwak=톱밥 묻은 캔버스 앞치마·팔토시
- 배경 `junk_shop_in` 곽 영감 고물상 — 안 — 이 씬 카메라 자리: `front_wide`(마당에서 열린 전면 안쪽으로 와이드(북향). 작업대 오른쪽, 공방 문 뒤 왼쪽), `bench_reverse`(작업대 안쪽 끝(북)에서 열린 전면 쪽으로(남향). 작업대에 앉은 영감의 왼쪽 옆얼굴, 그 너머 문간이 밝게(역광), 문간에 선 사람) / 그 밖: `east_wall_west`, `shelf_pov`, `exit_back`
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: 없음 / 그 밖: `door_wide`, `bench_reverse`, `kwak_back`, `bench_top`, `plank_gap`
- 소품: `dongguri__s3_fork_replaced`(동그리(깡통 바이올린 1호)·포크만 갈아 끼움(곽 영감 수리)), `scrap_sack`(고물 자루), `cotton_work_gloves`(목장갑), `rubber_boots`(고무장화(작업용)), `workbench`(곽 영감의 작업대(서랍 포함)), `wrap_cloth`(동그리를 싼 천), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방)

## 2-14 몽타주 — 공방 / 둑길 / 판잣집 (늦가을~초겨울)
- 빛: 1·2: 공방 판자 틈 빛, 실내 그늘. 3: 해 질 녘 둑길, 오른쪽(서쪽) 낮은 해. 4: 판잣집 실내 백열전구. 5: 천막 뒤, 흐린 낮
- 인물·의상: eunju=남색 점퍼·회색 손뜨개 목도리·목장갑(겨울); seonyoung=베이지 더플코트·목도리(늦가을~겨울); dongmin=물려받은 누빈 갈색 점퍼·털모자(겨울); manseok=낡은 야전상의·목수건·고무장화; deoksu=체크 남방 위 회색 털스웨터(겨울); mija=빨간 누빔 점퍼(겨울)
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `door_wide`(문(남)에서 안쪽으로 와이드(북향). 작업대 정면 안쪽, 창 왼쪽, 선반 오른쪽) / 그 밖: `bench_reverse`, `kwak_back`, `bench_top`, `plank_gap`
- 배경 `soup_tent_back` 국밥집 천막 — 뒤 쓰레기 더미 — 이 씬 카메라 자리: `path_south`(마을 흙길에서 천막 뒤와 더미(남향)) / 그 밖: `rear_flap`, `far_window`
- 배경 `shack_main` 은주네 판잣집 — 부엌 겸 방 — 이 씬 카메라 자리: 없음 / 그 밖: `door_wide`, `table_front`, `section`, `door_close`
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `middle_wide`(둑길 한가운데 작아지는 사람, 와이드(남향)) / 그 밖: `island_end_south`, `bank_side`, `low_shoes`
- 배경 `shack_village` 판잣집 동네 외경 — 이 씬 카메라 자리: `alley_west`(골목 안에서 서쪽으로: 오른쪽에 은주네 집 현관) / 그 밖: `roofs_to_entrance`
- 소품: `dongguri__s3_fork_replaced`(동그리(깡통 바이올린 1호)·포크만 갈아 끼움(곽 영감 수리)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `wrap_cloth`(동그리를 싼 천), `handcart`(리어카), `glasses_seonyoung`(선영의 동그란 금테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `deoksu_check_shirt`(덕수의 체크 남방)

## 2-15 국밥집 천막 (저녁, 1988년 1월)
- 빛: Insert(게시판): 흐린 겨울 낮. 천막 안: 저녁, 연탄난로 불빛과 천막 전구, 입김이 하얗게
- 인물·의상: choi=회색 양복 위 감색 오버코트(겨울); eunju=남색 점퍼·회색 손뜨개 목도리·목장갑(겨울); dongmin=물려받은 누빈 갈색 점퍼·털모자(겨울); manseok=낡은 야전상의·목수건·고무장화; mija=빨간 누빔 점퍼(겨울); deoksu=체크 남방 위 회색 털스웨터(겨울); sunrye=솜 누빈 조끼·털목도리(겨울); extra:미자 엄마·섬 아저씨·갈고리 아주머니·섬사람들=어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준), 겨울
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `entrance_wide`(앞자락(남)에서 안쪽으로 와이드(북향). 국솥 정면 안쪽, 기둥 가운데, 걷힌 옆자락 오른쪽), `pot_reverse`(국솥 쪽에서 앞자락 쪽으로(남향). 문간에 선 사람, 빈 입구) / 그 밖: `side_to_shop`, `band_front`, `bench_end`
- 배경 `notice_board` 섬 어귀 게시판 — 이 씬 카메라 자리: `thumbtack_close`(압정 머리·종이 귀퉁이 극접사) / 그 밖: `board_front`, `over_shoulder`, `road_north`
- 소품: `choi_handkerchief__s2_damp`(최 계장의 손수건·땀에 젖은 손수건), `pyeongsang`(평상), `soup_tent`(국밥집 천막), `notice_board`(섬 어귀 나무 게시판), `choi_envelope`(최 계장의 누런 서류 봉투), `glasses_choi`(최 계장의 검은 뿔테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `deoksu_check_shirt`(덕수의 체크 남방), `choi_gray_suit`(최 계장의 회색 양복), `notice_1988_jan`(1988년 1월 정식 통보 공문(빨간 도장 둘)), `coal_stove_kettle`(천막 연탄난로와 주전자)

## 2-16 둑길 (밤)
- 빛: 밤, 어둠. 천막·판잣집 쪽 먼 불빛이 낮게, 차가운 남청
- 인물·의상: mija=빨간 누빔 점퍼(겨울); eunju=남색 점퍼·회색 손뜨개 목도리·목장갑(겨울); dongmin=물려받은 누빈 갈색 점퍼·털모자(겨울)
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: `island_end_south`(섬 쪽 끝에서 뭍 쪽으로(남향) 고정. 멀리 다가오는 사람) / 그 밖: `bank_side`, `middle_wide`, `low_shoes`
- 소품: `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kicked_can`(미자가 걷어찬 깡통)

## 2-17 공방 (겨울, 낮)
- 빛: 판자 틈으로 드는 차가운 겨울 낮빛 + 가운데 연탄 화덕의 주황 불빛
- 인물·의상: kwak=앞치마 위 회색 털조끼·털모자(겨울); eunju=남색 점퍼·회색 손뜨개 목도리·손끝 자른 목장갑(겨울)
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `plank_gap`(서쪽 판자 틈에서 강 쪽으로(서향)) / 그 밖: `door_wide`, `bench_reverse`, `kwak_back`, `bench_top`
- 소품: `dongguri__s3_fork_replaced`(동그리(깡통 바이올린 1호)·포크만 갈아 끼움(곽 영감 수리)), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `reading_glasses_kwak`(곽 영감의 돋보기안경), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `coal_brazier`(공방 연탄 화덕), `scissors`(곽 영감의 가위), `fingerless_gloves`(손끝 자른 목장갑)
- 소리 색 순간(이 컷들에만): M: 동그리 가락 #F5C04A — 판자 틈으로 새어 나가 바람 따라 강 쪽으로 흐르는 빛 띠

## 2-18 학교 강당 (낮, 1988년 4월 셋째 주)
- 빛: 강당 무대 조명(정면 위), 무대 옆 커튼 뒤는 어둑, 객석은 높은 창의 낮빛
- 인물·의상: eunju=흰 블라우스·감색 치마(학교); deoksu=늘어난 흰 러닝셔츠 위 체크 남방; dongmin=흰 반소매 남방·감색 반바지(제일 좋은 옷); mija=새것 같은 빨간 트레이닝 위아래(제일 좋은 옷); seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; taejun=사립학교 교복(감색 재킷·넥타이); extra:객석(교복·학부모)·사회자=학생 대부분은 사복(1980년대 국민학교 자유복, 중학교 교복은 학교마다 달랐음), 일부 사립학교 교복, 학부모는 1980년대 외출복
- 배경 `school_auditorium` 학교 강당 — 이 씬 카메라 자리: `back_to_stage`(뒷문에서 무대 쪽 와이드), `wing_gap_to_house`(무대 옆 커튼 틈에서 객석을 훑어 문까지(은주 시점)) / 그 밖: `closed_door`
- 소품: `dongguri__s3_fork_replaced`(동그리(깡통 바이올린 1호)·포크만 갈아 끼움(곽 영감 수리)), `ttungbo__s2_complete`(뚱보(기름통 첼로)·완성(굵은 줄)), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s2_under_blouse`(은색 소리굽쇠 목걸이·블라우스 안 — 사슬만 보임), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_school_blouse`(은주의 빛바랜 흰 블라우스·감색 치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `taejun_uniform`(태준의 다솜중 교복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `auditorium_curtain`(학교 강당 무대 커튼)
- 소리 색 순간(이 컷들에만): M: 동그리 「도라지 타령」 #F5C04A — 은주 정면, 웃음소리가 한 겹씩 빠짐, 객석이 잠시 조용

## 2-19 학교 강당 (저녁)
- 빛: 저녁, 강당 무대 조명과 실내등, 창밖은 어두워짐. 은주 귀로 웃음이 갈라지는 컷: 화면 채도만 낮춤(색이 빠지는 쪽), 소리 색 없음
- 인물·의상: eunju=흰 블라우스·감색 치마(학교); seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; mija=새것 같은 빨간 트레이닝 위아래(제일 좋은 옷); dongmin=흰 반소매 남방·감색 반바지(제일 좋은 옷); deoksu=늘어난 흰 러닝셔츠 위 체크 남방; extra:사회자·객석=-
- 배경 `school_auditorium` 학교 강당 — 이 씬 카메라 자리: `back_to_stage`(뒷문에서 무대 쪽 와이드), `closed_door`(닫힌 뒷문 고정) / 그 밖: `wing_gap_to_house`
- 소품: `tuning_fork_necklace__s2_under_blouse`(은색 소리굽쇠 목걸이·블라우스 안 — 사슬만 보임), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_school_blouse`(은주의 빛바랜 흰 블라우스·감색 치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `emcee_paper`(사회자의 종이)

## 2-20 국밥집 천막 (아침, 이튿날)
- 빛: 아침, 천막 천 확산광, 국밥 김
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; sunrye=몸뻬 바지·꽃무늬 앞치마; extra:집하장 아저씨·갈고리 아주머니·섬 아저씨·섬사람들=어둡고 두꺼운 작업복, 머릿수건, 빨강·파랑 웃옷이 드문드문(research/notes 시각 고증 [A]14·18쪽 기준)
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `bench_end`(동쪽 평상 남쪽 끝(평상 끝) 가까이: 국밥 그릇·접힌 신문) / 그 밖: `entrance_wide`, `pot_reverse`, `side_to_shop`, `band_front`
- 소품: `newspaper_seoulmaeil__s1_open`(신문 「한강신보」 사회면 단신·평상에 펼친 신문), `newspaper_seoulmaeil__s2_folded`(신문 「한강신보」 사회면 단신·기사가 위로 오게 접힌 신문), `bowls_spoons`(밥그릇·국그릇·숟가락·젓가락), `pyeongsang`(평상), `soup_tent`(국밥집 천막), `hair_tie`(은주의 머리 고무줄), `gukbap`(국밥(뚝배기)), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마)
- 소리 색 순간(이 컷들에만): 숟가락이 국그릇에 닿는 '딸그락' #9DB7C9 — 주변 소리 빠지고 그 소리만 크게

## 2-21 국밥집 천막 (점심)
- 빛: 한낮, 천막 천 확산광. 손대지 않은 국밥 김이 가늘어짐
- 인물·의상: manseok=낡은 야전상의·목수건·고무장화; sunrye=몸뻬 바지·꽃무늬 앞치마
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `bench_end`(동쪽 평상 남쪽 끝(평상 끝) 가까이: 국밥 그릇·접힌 신문) / 그 밖: `entrance_wide`, `pot_reverse`, `side_to_shop`, `band_front`
- 소품: `newspaper_seoulmaeil__s2_folded`(신문 「한강신보」 사회면 단신·기사가 위로 오게 접힌 신문), `scrap_money`(고물값 지폐·동전), `pyeongsang`(평상), `soup_tent`(국밥집 천막), `work_cap_manseok`(만석의 국방색 작업모), `gukbap`(국밥(뚝배기)), `manseok_field_jacket`(만석의 낡은 야전상의), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마)

## 2-22 공방 (해 질 무렵)
- 빛: 해 질 무렵, 판자 틈으로 낮고 붉은 빛(서쪽), 영감 등은 역광 실루엣에 가까움
- 인물·의상: kwak=톱밥 묻은 캔버스 앞치마·팔토시; eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `kwak_back`(문 쪽에서 작업대에 앉은 사람의 등(북향, 가까이)) / 그 밖: `door_wide`, `bench_reverse`, `bench_top`, `plank_gap`
- 소품: `dongguri__s3_fork_replaced`(동그리(깡통 바이올린 1호)·포크만 갈아 끼움(곽 영감 수리)), `workbench`(곽 영감의 작업대(서랍 포함)), `sandpaper`(사포), `reading_glasses_kwak`(곽 영감의 돋보기안경), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시)

## 2-23 작은 산 꼭대기 (해 질 녘)
- 빛: 해 질 녘이지만 강 너머 하늘이 흙탕물 색으로 탁하게 저묾 — 1-11 같은 금빛 없음. 확산광, 그림자 흐림
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; mija=빨간 트레이닝 상의
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: `top_south`(꼭대기 가운데에서 남쪽(판자·마을·둑길·뭍)으로 와이드), `slope_up`(남쪽 비탈 아래에서 꼭대기 가장자리로 올려다봄(북향). 오르는 사람 등 너머 아이들 얼굴), `board_close`(꼭대기 판자 위(동그리 자리) 가까이·극접사), `sky_low`(하늘을 등진 앙각(미자, 비닐))
- 소품: `dongguri__s4_abandoned`(동그리(깡통 바이올린 1호)·버려짐 — 줄 풀림(작은 산 판자 위)), `rubber_boots`(고무장화(작업용)), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `flat_board`(작은 산 꼭대기의 납작한 판자), `white_vinyl`(쓰레기 산의 흰 비닐 조각), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `mija_red_tracksuit`(미자의 빨간 트레이닝)

## 2-24 은주네 판잣집, 부엌 겸 방 (저녁)
- 빛: 판잣집 실내 백열전구 하나, 어둑하고 무거운 톤
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; manseok=낡은 야전상의·목수건·고무장화
- 배경 `shack_main` 은주네 판잣집 — 부엌 겸 방 — 이 씬 카메라 자리: `door_wide`(현관문 안에서 방 안쪽으로(북향). 작은 창·곤로 왼쪽, 합판 벽·쪽방 문 오른쪽 안) / 그 밖: `table_front`, `section`, `door_close`
- 소품: `low_table`(밥상(접이식 낮은 상)), `bowls_spoons`(밥그릇·국그릇·숟가락·젓가락), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `dongmin_tracksuit`(동민의 물려받은 큰 운동복)

## 2-25 은주네 판잣집, 쪽방 (밤)
- 빛: 쪽방 백열전구 → 불 끈 뒤 깊은 남색 어둠
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; manseok=낡은 야전상의·목수건·고무장화
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: `door_south`(쪽방 문에서 방 끝 작은 창 쪽으로(남향). 합판 벽 오른쪽, 선반 왼쪽 안), `wall_close`(합판 벽과 손가락 마디 극접사(톡톡)), `section`(두 칸 단면(shack_main의 section과 같은 그림)) / 그 밖: `top_down`, `window_from_mat`
- 소품: `tuning_fork_necklace__s3_in_box`(은색 소리굽쇠 목걸이·라디오 상자 속 — 엉킨 사슬), `mother_radio__s1_broken`(엄마의 고장 난 트랜지스터라디오·고장 — 은주가 고쳐 보는 라디오), `radio_box__s1_closed`(라디오 상자(나무 상자)·선반 위 닫힌 상자), `radio_box__s2_open`(라디오 상자(나무 상자)·열린 상자 — 라디오와 엉킨 사슬), `blanket`(이불), `plywood_wall`(합판 벽(판잣집 칸막이)), `work_cap_manseok`(만석의 국방색 작업모), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의)

## 2-26 은주네 판잣집, 부엌 겸 방 (밤, 자정 지나)
- 빛: 거의 어둠, 창의 희미한 남색 밤빛만
- 인물·의상: manseok=낡은 야전상의·목수건·고무장화; dongmin=물려받은 큰 운동복
- 배경 `shack_main` 은주네 판잣집 — 부엌 겸 방 — 이 씬 카메라 자리: `door_close`(현관문 안쪽 문고리·목수건·못의 손전등 가까이) / 그 밖: `door_wide`, `table_front`, `section`
- 소품: `rubber_boots`(고무장화(작업용)), `flashlight`(손전등), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `shack_door`(판잣집 문과 문고리), `manseok_field_jacket`(만석의 낡은 야전상의), `dongmin_tracksuit`(동민의 물려받은 큰 운동복)

## 2-27 작은 산 (깊은 밤)
- 빛: 손전등 원 하나가 유일한 광원(따뜻한 노랑), 나머지는 남색 어둠. 큰 산 검은 등성이 위 별
- 인물·의상: manseok=낡은 야전상의·목수건·고무장화
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: `slope_up`(남쪽 비탈 아래에서 꼭대기 가장자리로 올려다봄(북향). 오르는 사람 등 너머 아이들 얼굴), `board_close`(꼭대기 판자 위(동그리 자리) 가까이·극접사) / 그 밖: `top_south`, `sky_low`
- 배경 `small_hill_slope` 작은 산 중턱 — 이 씬 카메라 자리: `slope_from_below_night`(비탈 아래에서 올라가는 작은 불빛 하나(롱, 북향)) / 그 밖: `slope_down_se`, `slope_wide`
- 소품: `dongguri__s4_abandoned`(동그리(깡통 바이올린 1호)·버려짐 — 줄 풀림(작은 산 판자 위)), `rubber_boots`(고무장화(작업용)), `flashlight`(손전등), `work_cap_manseok`(만석의 국방색 작업모), `flat_board`(작은 산 꼭대기의 납작한 판자), `white_vinyl`(쓰레기 산의 흰 비닐 조각), `manseok_field_jacket`(만석의 낡은 야전상의), `broken_flowerpot_shoe`(손전등 원 안의 깨진 화분·고무신 한 짝)

## 2-28 곽 영감 고물상 앞 (깊은 밤)
- 빛: 어둠 속 고물상 문틈·창으로 번지는 노란 백열등 한 줄기, 영감은 그 빛을 등짐. 높은 와이드에서 섬 전체에 불 켜진 곳은 거기 하나
- 인물·의상: manseok=낡은 야전상의·목수건·고무장화; kwak=톱밥 묻은 캔버스 앞치마·팔토시
- 배경 `junk_shop_in` 곽 영감 고물상 — 안 — 이 씬 카메라 자리: 없음 / 그 밖: `front_wide`, `bench_reverse`, `east_wall_west`, `shelf_pov`, `exit_back`
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `yard_front`(마당(둑길 끝)에서 고물상 전면으로(북향) 외경) / 그 밖: `from_tent`, `village_south`
- 배경 `island_wide` 갈대섬 전경 — 이 씬 카메라 자리: `high_north`(뭍 쪽 하늘에서 섬 전체를 북향으로 내려다보는 높은 와이드)
- 소품: `dongguri__s4_abandoned`(동그리(깡통 바이올린 1호)·버려짐 — 줄 풀림(작은 산 판자 위)), `apple_crate`(빈 사과 상자), `reading_glasses_kwak`(곽 영감의 돋보기안경), `work_cap_manseok`(만석의 국방색 작업모), `manseok_field_jacket`(만석의 낡은 야전상의), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시)

## 2-29 은주네 판잣집, 쪽방 (깊은 밤, 같은 시각)
- 빛: 거의 어둠, 남색. 은주 귀에만 아주 희미한 빛
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: 없음 / 그 밖: `top_down`, `door_south`, `window_from_mat`, `wall_close`, `section`
- 소품: `blanket`(이불), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼)

## 3-1 곽 영감 고물상 (낮, 1988년 5월)
- 빛: 오월 한낮 맑은 햇빛, 위·왼쪽에서, 고물 쇠붙이 위 반짝임. 회상 Insert: 한밤 고물상, 노란 백열등 하나(위), 둘레는 남색 어둠
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; kwak=톱밥 묻은 캔버스 앞치마·팔토시; manseok=낡은 야전상의·목수건·고무장화
- 배경 `junk_shop_in` 곽 영감 고물상 — 안 — 이 씬 카메라 자리: `front_wide`(마당에서 열린 전면 안쪽으로 와이드(북향). 작업대 오른쪽, 공방 문 뒤 왼쪽) / 그 밖: `bench_reverse`, `east_wall_west`, `shelf_pov`, `exit_back`
- 배경 `junk_shop_front` 곽 영감 고물상 — 앞(외경) — 이 씬 카메라 자리: `yard_front`(마당(둑길 끝)에서 고물상 전면으로(북향) 외경) / 그 밖: `from_tent`, `village_south`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `scrap_sack`(고물 자루), `cotton_work_gloves`(목장갑), `hanging_scale`(걸이 저울(고물상)), `workbench`(곽 영감의 작업대(서랍 포함)), `scrap_money`(고물값 지폐·동전), `bulb`(백열전구), `tin_roof`(고물상 함석지붕), `apple_crate`(빈 사과 상자), `kwak_pencil`(곽 영감이 귀에 꽂은 연필), `reading_glasses_kwak`(곽 영감의 돋보기안경), `work_cap_manseok`(만석의 국방색 작업모), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `glue_brush`(곽 영감의 아교 붓)
- 소리 색 순간(이 컷들에만): 동그리 '동—' 금빛 #F5C04A — 은주가 맨손가락으로 몸통을 톡 건드린 컷(대본: 주변 소리 빠지고 그 소리만 남는다, 처음 그날과 같은 울림)

## 3-2 은주네 판잣집, 부엌 겸 방 (저녁)
- 빛: 작은 창으로 들어오는 저녁 잔광(왼쪽, 주황빛) + 석유곤로의 푸른 불꽃, 방 안은 따뜻한 어스름
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; dongmin=물려받은 큰 운동복; manseok=낡은 야전상의·목수건·고무장화
- 배경 `shack_main` 은주네 판잣집 — 부엌 겸 방 — 이 씬 카메라 자리: `door_wide`(현관문 안에서 방 안쪽으로(북향). 작은 창·곤로 왼쪽, 합판 벽·쪽방 문 오른쪽 안), `table_front`(방 안쪽(북쪽)에서 밥상 정면, 뒤로 현관문(남향). 세 사람 밥상 정면) / 그 밖: `section`, `door_close`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `rubber_boots`(고무장화(작업용)), `kerosene_stove`(석유곤로와 냄비), `low_table`(밥상(접이식 낮은 상)), `bowls_spoons`(밥그릇·국그릇·숟가락·젓가락), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `shack_door`(판잣집 문과 문고리), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `doenjang_jjigae`(된장찌개)

## 3-3 은주네 판잣집, 부엌 겸 방 (밤)
- 빛: 곤로 불 꺼짐, 백열등 하나(위 가운데) — 밥상 자리에 따뜻한 노란 원, 구석은 남색 그늘. 회상(극장 2컷): 세피아, 무대 쪽 스포트 역광과 반짝이 막의 반사, 엄마 얼굴은 무대 조명에 가려 보이지 않음
- 인물·의상: manseok=낡은 야전상의·목수건·고무장화; eunju=큰 남색 점퍼·해진 바지·목장갑; extra:엄마 한미숙(회상, 얼굴 금지)=회상 — 대본 근거 없음; dongmin=물려받은 큰 운동복
- 배경 `shack_main` 은주네 판잣집 — 부엌 겸 방 — 이 씬 카메라 자리: `table_front`(방 안쪽(북쪽)에서 밥상 정면, 뒤로 현관문(남향). 세 사람 밥상 정면) / 그 밖: `door_wide`, `section`, `door_close`
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: 없음 / 그 밖: `top_down`, `door_south`, `window_from_mat`, `wall_close`, `section`
- 배경 `fb_theater` 회상: 1970년대 극장 쇼 무대 — 이 씬 카메라 자리: `front_to_band`(무대 앞에서 뒤쪽 악단석으로 천천히)
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `tuning_fork_necklace__s3_in_box`(은색 소리굽쇠 목걸이·라디오 상자 속 — 엉킨 사슬), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `mother_radio__s1_broken`(엄마의 고장 난 트랜지스터라디오·고장 — 은주가 고쳐 보는 라디오), `radio_box__s1_closed`(라디오 상자(나무 상자)·선반 위 닫힌 상자), `radio_box__s2_open`(라디오 상자(나무 상자)·열린 상자 — 라디오와 엉킨 사슬), `manseok_clarinet__s1_1970s`(만석의 클라리넷·회상 — 1970년대 극장 쇼 악단), `pawn_ticket_manseok__s1`(만석의 전당표·닳은 전당표), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `kerosene_stove`(석유곤로와 냄비), `low_table`(밥상(접이식 낮은 상)), `bowls_spoons`(밥그릇·국그릇·숟가락·젓가락), `bulb`(백열전구), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `manseok_field_jacket`(만석의 낡은 야전상의), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `theater_stage_1970s`(1970년대 극장 쇼 무대의 반짝이 막과 악단 보면대)
- 소리 색 순간(이 컷들에만): 회상 극장 악단 반주(M:) — 만석의 클라리넷 와인색 #9C4A6B, 세피아 화면 위 악단석의 클라리넷에서만 / 소리굽쇠 '웅―' 은빛 흰색 #E9EEF5 — 목걸이를 건 뒤 은주가 손톱으로 튕기는 컷, 빛 띠가 방을 한 바퀴 / 동그리 짧은 음 금빛 #F5C04A — M: 방바닥에 떨어지듯 작게. 빛도 작게, 동그리 둘레만

## 3-4 작은 산 꼭대기 (새벽)
- 빛: 해 뜨기 전 회청색 산광, 동쪽 지평선만 옅게 밝음, 그림자 거의 없음. 둑길 저편에 첫 트럭 헤드라이트 두 점
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: `top_south`(꼭대기 가운데에서 남쪽(판자·마을·둑길·뭍)으로 와이드) / 그 밖: `slope_up`, `board_close`, `sky_low`
- 소품: `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `cotton_work_gloves`(목장갑), `rubber_boots`(고무장화(작업용)), `composition_notebook`(선영 선생이 준 공책), `pencil`(연필(은주·선영)), `hair_tie`(은주의 머리 고무줄), `eunju_navy_jumper`(은주의 큰 남색 점퍼)
- 소리 색 순간(이 컷들에만): 소리굽쇠 '웅―' 은빛 흰색 #E9EEF5 — 라(대본: 바람 소리 빠지고 라와 엔진 두 겹만 남는다) / 첫 트럭 엔진 '그르르르' 연청색 #9DB7C9 — 둑길 저편에서 땅을 타고 올라오는 낮은 물결 띠(2절 '은주의 귀' 색: 대본 '라와 엔진 두 겹만 남는다')

## 3-5 공방 (같은 날 오후)
- 빛: 오후 햇빛이 공방 문과 작은 창으로 비스듬히(왼쪽), 톱밥 먼지가 빛줄기 속에 뜸
- 인물·의상: eunju=큰 남색 점퍼·해진 바지·목장갑; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; mija=빨간 트레이닝 상의; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; dongmin=물려받은 큰 운동복
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `door_wide`(문(남)에서 안쪽으로 와이드(북향). 작업대 정면 안쪽, 창 왼쪽, 선반 오른쪽) / 그 밖: `bench_reverse`, `kwak_back`, `bench_top`, `plank_gap`
- 소품: `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `workbench`(곽 영감의 작업대(서랍 포함)), `sawdust`(톱밥), `nurungji`(누룽지), `composition_notebook`(선영 선생이 준 공책), `staff_paper`(오선지), `pencil`(연필(은주·선영)), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `workshop_cans`(공방 선반의 깡통들), `eunju_navy_jumper`(은주의 큰 남색 점퍼), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트)

## 3-6 몽타주 — 섬의 소리를 모으다 (며칠, 섬 여러 곳)
- 빛: (1) 아침 큰 산 아래 쇳더미: 낮은 동쪽 아침 해, 뿌연 베이지 하늘 / (2~4) 공방 낮: 창으로 드는 햇빛 / (5~7) 작은 산 꼭대기 한낮: 머리 위 강한 해, 짧은 그림자, 비닐이 나부끼는 바람 / (8~9) 국밥집 천막 저녁: 해 질 녘 주황 잔광 + 국솥 연탄불 / (10~11) 공방 저녁(추정): 백열등
- 인물·의상: eunju=빛바랜 하늘색 반소매 셔츠·해진 바지(여름); dongmin=물려받은 큰 운동복; mija=빨간 트레이닝 상의; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; seonyoung=구겨진 흰 셔츠·카디건·긴 플레어스커트; sunrye=몸뻬 바지·꽃무늬 앞치마
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: 없음 / 그 밖: `door_wide`, `bench_reverse`, `kwak_back`, `bench_top`, `plank_gap`
- 배경 `soup_tent_in` 국밥집 천막 — 안 — 이 씬 카메라 자리: `entrance_wide`(앞자락(남)에서 안쪽으로 와이드(북향). 국솥 정면 안쪽, 기둥 가운데, 걷힌 옆자락 오른쪽) / 그 밖: `pot_reverse`, `side_to_shop`, `band_front`, `bench_end`
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: `top_south`(꼭대기 가운데에서 남쪽(판자·마을·둑길·뭍)으로 와이드), `sky_low`(하늘을 등진 앙각(미자, 비닐)) / 그 밖: `slope_up`, `board_close`
- 배경 `scrap_heap` 큰 산 아래 쇳더미 — 이 씬 카메라 자리: `heap_pan`(은주 시점, 더미를 천천히 훑는 팬) / 그 밖: `heap_up`, `from_small_hill`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `sunrye_ladle__s2_borrowed`(순례 할머니의 국자·덕수가 빌려 간 국자(악기)), `soup_pot__s1`(국솥(국밥집 무쇠 솥)·김이 오르는 솥), `cotton_work_gloves`(목장갑), `soup_tent`(국밥집 천막), `staff_paper`(오선지), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `white_vinyl`(쓰레기 산의 흰 비닐 조각), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `seonyoung_outfit`(선영의 흰 셔츠·카디건·플레어스커트), `copper_pipe_and_pot`(구리 파이프와 양은 냄비(소리 고르기))

## 3-7 은주네 판잣집, 쪽방 (밤)
- 빛: 불 꺼진 쪽방, 작은 창으로 들어오는 남색 밤빛 한 줄, 그 밖의 광원 없음
- 인물·의상: eunju=빛바랜 하늘색 반소매 셔츠·해진 바지(여름)
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: `door_south`(쪽방 문에서 방 끝 작은 창 쪽으로(남향). 합판 벽 오른쪽, 선반 왼쪽 안) / 그 밖: `top_down`, `window_from_mat`, `wall_close`, `section`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `mother_radio__s1_broken`(엄마의 고장 난 트랜지스터라디오·고장 — 은주가 고쳐 보는 라디오), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `blanket`(이불), `hair_tie`(은주의 머리 고무줄)
- 소리 색 순간(이 컷들에만): 라디오 허밍 연보라 #B9A7D9 — 지직거림 빠지고 허밍 네 음만 남는 컷, 라디오 스피커에서 가는 연보라 동심원 / 동그리 금빛 #F5C04A — M: 허밍 네 음을 따라 작게. 연보라 띠 옆에 가는 금빛 띠가 나란히

## 3-8 공방 (낮)
- 빛: 낮, 공방 창과 문으로 드는 햇빛(왼쪽), 톱밥 먼지
- 인물·의상: eunju=빛바랜 하늘색 반소매 셔츠·해진 바지(여름); seonyoung=구겨진 흰 반소매 블라우스·긴 플레어스커트(여름); dongmin=초록 반소매 체육복 티·반바지(여름); mija=빨간 반소매 티(여름); deoksu=흰 러닝셔츠·반바지(여름)
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: 없음 / 그 밖: `door_wide`, `bench_reverse`, `kwak_back`, `bench_top`, `plank_gap`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `staff_paper`(오선지), `pencil`(연필(은주·선영)), `glasses_seonyoung`(선영의 동그란 금테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄)
- 소리 색 순간(이 컷들에만): 동그리 독주 금빛 #F5C04A — M: 허밍 네 음

## 3-9 공방 (사흘 뒤, 낮)
- 빛: 낮, 공방 창 햇빛(왼쪽). 문틈 컷은 안쪽 어둑함에 문틈 바깥 빛이 세로 한 줄
- 인물·의상: eunju=빛바랜 하늘색 반소매 셔츠·해진 바지(여름); mija=빨간 반소매 티(여름); kwak=앞치마·반소매 작업 셔츠(여름); dongmin=초록 반소매 체육복 티·반바지(여름); bonggu=노란 러닝셔츠·반바지; yeongran=분홍 반소매 블라우스·감색 치마; gyeongho=파란 티·반바지; gyeongmin=주황 티·반바지; suni=꽃무늬 원피스; seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `door_wide`(문(남)에서 안쪽으로 와이드(북향). 작업대 정면 안쪽, 창 왼쪽, 선반 오른쪽), `bench_reverse`(작업대 쪽에서 문 쪽으로(남향). 문가에 선 사람 역광, 문틈, 사다리), `bench_top`(작업대 위 부감) / 그 밖: `kwak_back`, `plank_gap`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `can_violin_2__s1`(깡통 바이올린 2호(봉구)·완성(3-9 이후)), `can_violin_3__s1`(깡통 바이올린 3호(영란)·완성(3-9 이후)), `pot_lid_cymbals__s1`(냄비 뚜껑 심벌(경호·경민)·쌍둥이가 받은 그대로), `bottle_xylophone__s1`(병 실로폰(순이·석이)·물 높이를 맞춘 완성), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `cotton_work_gloves`(목장갑), `workbench`(곽 영감의 작업대(서랍 포함)), `piano_wire`(피아노 쇠줄 다발), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `can_sack_3_9`(깡통 한 자루), `chosen_can`(은주가 고른 맑은 깡통)
- 소리 색 순간(이 컷들에만): 고른 깡통 '톡' 연청 #9DB7C9(은주의 귀) — 대본: 주변 소리 빠지고 그 소리만 남는다. 은주 손끝의 깡통에서만

## 3-10 공방 (저녁, 1988년 6월 끝)
- 빛: 창밖 해 질 녘 → 점점 어두워짐(대본), 안은 백열등. 문가 만석은 바깥 잔광 역광. 회상(예선, 짧게): 객석이 하얗게 번진 무대 빛. 회상 Insert 전당포: 누런 형광등
- 인물·의상: eunju=빛바랜 하늘색 반소매 셔츠·해진 바지(여름); seonyoung=구겨진 흰 반소매 블라우스·긴 플레어스커트(여름); mija=빨간 반소매 티(여름); deoksu=흰 러닝셔츠·반바지(여름); dongmin=초록 반소매 체육복 티·반바지(여름); bonggu=노란 러닝셔츠·반바지; yeongran=분홍 반소매 블라우스·감색 치마; gyeongho=파란 티·반바지; gyeongmin=주황 티·반바지; suni=꽃무늬 원피스; seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자; manseok=낡은 야전상의·목수건·고무장화
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `door_wide`(문(남)에서 안쪽으로 와이드(북향). 작업대 정면 안쪽, 창 왼쪽, 선반 오른쪽), `bench_reverse`(작업대 쪽에서 문 쪽으로(남향). 문가에 선 사람 역광, 문틈, 사다리) / 그 밖: `kwak_back`, `bench_top`, `plank_gap`
- 배경 `pawnshop` 만복전당포 — 이 씬 카메라 자리: `counter_reverse`(계산대 뒤 주인 자리에서 문 쪽으로(문 종, 들어오는 사람)) / 그 밖: `door_in`, `counter_top`
- 배경 `school_auditorium` 학교 강당 — 이 씬 카메라 자리: 없음 / 그 밖: `back_to_stage`, `wing_gap_to_house`, `closed_door`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `can_violin_2__s1`(깡통 바이올린 2호(봉구)·완성(3-9 이후)), `can_violin_3__s1`(깡통 바이올린 3호(영란)·완성(3-9 이후)), `pot_lid_cymbals__s1`(냄비 뚜껑 심벌(경호·경민)·쌍둥이가 받은 그대로), `bottle_xylophone__s1`(병 실로폰(순이·석이)·물 높이를 맞춘 완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `empty_violin_case__s4_workshop`(선영의 빈 바이올린 케이스·공방 작업대 위 열린 케이스(3-10)), `newspaper_seoulmaeil__s3_flash`(신문 「한강신보」 사회면 단신·회상 극접사 — 단신 제목), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `drumstick_spoons`(북채(나무 숟가락 두 개)), `workbench`(곽 영감의 작업대(서랍 포함)), `sheet_music`(선영의 악보), `candy`(알록달록 사탕), `apple_crate`(빈 사과 상자), `staff_paper`(오선지), `pencil`(연필(은주·선영)), `glasses_seonyoung`(선영의 동그란 금테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `manseok_field_jacket`(만석의 낡은 야전상의)
- 소리 색 순간(이 컷들에만): 리허설 M: 「섬의 하루」 — 악기 둘레에만 아주 작은 빛 점(새벽 주황 #E8944A, 아침 금빛 #F5C04A·빨강 #D9534A, 한낮 청록 #4FB3A9). 주변 채도 낮춤 없음, 화면으로 번지지 않음(온전히 색이 차는 것은 본선 S#25 '밤'에만)

## 3-11 공방 구석 (같은 날 밤)
- 빛: 공방 구석, 멀리 백열등 하나의 빛만 닿음, 나머지 어둠
- 인물·의상: mija=빨간 반소매 티(여름)
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: 없음 / 그 밖: `door_wide`, `bench_reverse`, `kwak_back`, `bench_top`, `plank_gap`
- 소품: `mija_savings_can__s1_first_coin`(미자의 '찾을 돈' 깡통·첫 동전(3-11)), `scrap_money`(고물값 지폐·동전), `bandage`(반창고(미자 코·동민 무릎)), `marker_pen`(미자의 굵은 펜)

## 3-12 구청 도시정비과 사무실 (낮, 1988년 7월 초)
- 빛: 하얀 형광등(위)에서 책상 줄로, 창 빛 약함. 회상 Insert 1(국밥집 앞 진흙): 흐린 낮. 회상 Insert 2(최 계장 어린 시절 판잣집): 빛바랜 색, 회색 빗빛
- 인물·의상: choi=흰 반소매 와이셔츠·넥타이, 양복 상의는 의자에(여름); extra:과장=대본 근거 없음 — 회색 양복 제안; extra:어린 최 계장(회상)=기워 입은 헐렁한 옷·맨발(1950년대 회상)
- 배경 `district_office` 구청 도시정비과 사무실 — 이 씬 카메라 자리: `light_down`(형광등에서 내려와 책상 줄로), `chief_desk`(과장 책상 앞에 선 최 계장(옆에서))
- 배경 `fb_shanty_1950s` 회상: 1950년대 판자촌 집 — 이 씬 카메라 자리: `bare_feet`(지붕 아래 쪼그린 작은 아이의 맨발)
- 소품: `choi_handkerchief__s2_damp`(최 계장의 손수건·땀에 젖은 손수건), `choi_shoes`(최 계장의 반들반들한 구두), `olympic_poster`(올림픽 표어 포스터(표어만)), `ballpoint_pen`(볼펜), `glasses_choi`(최 계장의 검은 뿔테 안경), `report_cover`(최 계장의 보고서(표지·본문)), `desk_fan`(구청 사무실 선풍기), `office_stamp`(과장의 결재 도장), `tin_roof_1950s`(회상: 어린 최 계장 판잣집의 양철 지붕)

## 3-13 구청 복도 (낮)
- 빛: 복도 형광등(위), 복도 끝 창의 흰 빛
- 인물·의상: choi=흰 반소매 와이셔츠·넥타이, 양복 상의는 의자에(여름)
- 배경 `district_corridor` 구청 복도 — 이 씬 카메라 자리: `plant_close`(화분 접사, 위에서 물방울)
- 소품: `choi_handkerchief__s2_damp`(최 계장의 손수건·땀에 젖은 손수건), `glasses_choi`(최 계장의 검은 뿔테 안경), `corridor_plant`(구청 복도 화분)

## 3-14 국밥집 천막 (이튿날 낮)
- 빛: 칠월 한낮 해(머리 위), 천막 앞 짧은 그림자, 천막 안은 천을 거른 부드러운 빛
- 인물·의상: choi=흰 반소매 와이셔츠·넥타이, 양복 상의는 의자에(여름); mija=빨간 반소매 티(여름); extra:미자 엄마=대본 근거 없음; sunrye=몸뻬 바지·꽃무늬 앞치마; extra:섬사람들=얇은 반소매 작업 셔츠·면바지·몸뻬, 머릿수건, 밀짚모자 드문드문(여름); bonggu=노란 러닝셔츠·반바지; yeongran=분홍 반소매 블라우스·감색 치마; gyeongho=파란 티·반바지; gyeongmin=주황 티·반바지; suni=꽃무늬 원피스; seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자
- 배경 `soup_tent_front` 국밥집 천막 — 앞 — 이 씬 카메라 자리: `yard_north`(마당에서 천막 앞으로 와이드(북향). 고물상은 오른쪽) / 그 밖: `front_east`, `low_mud`
- 소품: `choi_handkerchief__s1_dry`(최 계장의 손수건·마른 손수건), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `soup_pot__s1`(국솥(국밥집 무쇠 솥)·김이 오르는 솥), `soup_tent`(국밥집 천막), `thumbtacks`(압정과 압정 통), `glasses_choi`(최 계장의 검은 뿔테 안경), `bandage`(반창고(미자 코·동민 무릎)), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `relocation_notice`(천막 기둥에 붙인 이주 공문(1988년 7월))

## 3-15 공방 (밤, 본선 전날)
- 빛: 백열등 하나(작업대 위) — 작은 빛의 원, 나머지는 남색 어둠. 진짜 바이올린의 꿀빛 반사, 다락에서 내려온 먼지와 톱밥이 빛 속에 떠오름
- 인물·의상: eunju=빛바랜 하늘색 반소매 셔츠·해진 바지(여름); dongmin=초록 반소매 체육복 티·반바지(여름); kwak=앞치마·반소매 작업 셔츠(여름)
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `door_wide`(문(남)에서 안쪽으로 와이드(북향). 작업대 정면 안쪽, 창 왼쪽, 선반 오른쪽), `bench_reverse`(작업대 쪽에서 문 쪽으로(남향). 문가에 선 사람 역광, 문틈, 사다리), `bench_top`(작업대 위 부감) / 그 밖: `kwak_back`, `plank_gap`
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `kwak_violin__s1_wrapped`(곽 영감의 진짜 바이올린·다락의 천 꾸러미), `kwak_violin__s2_unwrapped`(곽 영감의 진짜 바이올린·천을 푼 바이올린), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `scrap_sack`(고물 자루), `workbench`(곽 영감의 작업대(서랍 포함)), `sawdust`(톱밥), `bulb`(백열전구), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `workshop_cans`(공방 선반의 깡통들), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `kwak_apron`(곽 영감의 캔버스 앞치마·팔토시), `ladder_attic`(고물상 사다리와 다락), `rag`(은주의 걸레)
- 소리 색 순간(이 컷들에만): 곽 영감의 진짜 바이올린 한 소절(M:) 차가운 청색 #5B8DEF — 매끄럽고 넓은 청색 띠가 강물처럼 벽과 천장까지 흐름, 떠오르는 톱밥 사이로 / 동그리 '동—' 금빛 #F5C04A — 은주가 깡통 몸통을 톡 치는 컷(대본: 주변 소리 빠지고 그 소리만)

## 3-16 한빛문화회관 앞 (낮, 1988년 7월 넷째 주 토요일)
- 빛: 한낮 머리 위 강한 햇볕, 광장 바닥이 하얗게 반사, 짧은 그림자. 계단 아래에서 올려다보는 구도라 하늘은 뿌연 흰빛
- 인물·의상: extra:섬사람들=대본: 다림질 자국 선명한 셔츠, 장롱 깊이 두었던 블라우스, 고무장화 대신 운동화; sunrye=외출용 자주색 블라우스·긴 치마, 접은 앞치마를 손에(본선); manseok=낡은 야전상의·다린 셔츠·운동화(본선)
- 배경 `hanbit_front` 한빛문화회관 앞·계단 — 이 씬 카메라 자리: `steps_up`(계단 아래에서 정면을 올려다봄), `plaza_wide`(광장의 전세 버스와 사람들, 노을 와이드) / 그 밖: `steps_down`
- 소품: `charter_bus`(낡은 전세 버스), `work_cap_manseok`(만석의 국방색 작업모), `manseok_field_jacket`(만석의 낡은 야전상의), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `bus_sign_galdaeseom`(전세 버스 앞 유리의 손글씨 종이 '갈대섬')

## 3-17 한빛문화회관 무대 뒤 복도 (낮)
- 빛: 좁은 복도 하얀 형광등(위, 대본), 복도 끝은 어둠
- 인물·의상: eunju=빌린 흰 원피스(무대)
- 배경 `hanbit_corridor` 한빛문화회관 무대 뒤 복도 — 이 씬 카메라 자리: `mirror_front`(거울 속 정면), `follow_dark`(뒤를 따라 복도 끝 어둠 속으로)
- 소품: `dongguri__s5_restored`(동그리(깡통 바이올린 1호)·다시 손봄(곽 영감·만석의 사흘 밤)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `hair_tie`(은주의 머리 고무줄), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `hallway_mirror`(무대 뒤 복도 거울)
- 소리 색 순간(이 컷들에만): 비발디 '여름' 3악장(M:, 벽 너머 먹먹하게) 차가운 청색 #5B8DEF, 아주 옅게 — 벽에서 번져 나오는 흐릿한 청색 띠

## 3-18 한빛문화회관 무대 옆, 커튼 뒤 (낮)
- 빛: 어둑한 무대 옆, 백열 작업등 하나(위, 노란 빛의 원). 무대 쪽에서 차갑고 좁은 하얀 조명이 칼날처럼 새어 듦(대본). 커튼 틈 시점 컷(다솜중 연주): 차갑고 좁은 흰 스포트가 검은 연주복 줄을 위에서 내리꽂음, 객석은 어둠(이 씬만 흰빛 — 섬 아이들 무대 S#19부터 따뜻한 스포트)
- 인물·의상: kwak=다린 흰 반소매 셔츠·회색 바지(본선); seonyoung=검은 연주복(무대); eunju=빌린 흰 원피스(무대); deoksu=단추를 목까지 잠근 체크 남방·빨간 손수건(본선); mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); dongmin=흰 반소매 남방·감색 반바지·빨간 손수건(본선); bonggu=노란 반소매 남방·반바지·빨간 손수건(본선); yeongran=분홍 반소매 블라우스·감색 치마·빨간 손수건(본선); gyeongho=파란 티·반바지·빨간 손수건(본선); gyeongmin=주황 티·반바지·빨간 손수건(본선); suni=꽃무늬 원피스·빨간 손수건(본선); seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선); taejun=검은 연주복; extra:다솜중 단원=검은 연주복
- 배경 `workshop` 공방(고물상 뒤) — 이 씬 카메라 자리: `bench_top`(작업대 위 부감) / 그 밖: `door_wide`, `bench_reverse`, `kwak_back`, `plank_gap`
- 배경 `hanbit_wing` 한빛문화회관 무대 옆, 커튼 뒤 — 이 씬 카메라 자리: `wing_to_stage`(무대 옆 안쪽에서 무대 쪽으로: 왼쪽 커튼 틈, 의자와 작업등), `curtain_gap_pov`(커튼 틈 시점: 무대 위 연주(은주 시점)) / 그 밖: `stage_to_wing`, `steps_down`
- 소품: `dongguri__s6_worn_e`(동그리(깡통 바이올린 1호)·본선 — E현이 닳음), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `can_violin_2__s1`(깡통 바이올린 2호(봉구)·완성(3-9 이후)), `can_violin_3__s1`(깡통 바이올린 3호(영란)·완성(3-9 이후)), `pot_lid_cymbals__s1`(냄비 뚜껑 심벌(경호·경민)·쌍둥이가 받은 그대로), `bottle_xylophone__s1`(병 실로폰(순이·석이)·물 높이를 맞춘 완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `taejun_violin__s1`(태준의 바이올린·변화 없음), `red_neckerchief__s1_flat`(빨간 손수건(본선 목 스카프)·펼친 천(만든 그대로)), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `workbench`(곽 영감의 작업대(서랍 포함)), `taejun_case`(태준의 고급 바이올린 케이스), `kwak_pencil`(곽 영감이 귀에 꽂은 연필), `glasses_seonyoung`(선영의 동그란 금테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `stage_curtain`(한빛문화회관 붉은 벨벳 커튼), `folding_chair`(접이식 의자), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `concert_black`(검은 연주복(다솜중·선영)), `empty_string_envelope`(작업대 서랍의 빈 줄 봉투)
- 소리 색 순간(이 컷들에만): 비발디 '여름' 3악장(M:, 폭풍) 차가운 청색 #5B8DEF, 옅게 — 다솜중 활들의 숲에서 가늘고 곧은 청색 띠(섬 악기 색보다 투명하게). 태준 왼손 손끝 극접사에서는 띠가 멀어짐

## 3-19 한빛문화회관 홀 — 무대·객석 (낮)
- 빛: 무대 위 따뜻한 호박빛 스포트(위·앞에서), 객석은 어둠 속 남색, 무대 나무 바닥에 따뜻한 반사. 은주 시점 컷: 조명 너머 객석이 하얗게 번짐(과노출). 회상 Insert(쪽방 벽 톡톡): 따뜻한 남색 밤, 짧게
- 인물·의상: eunju=빌린 흰 원피스(무대); seonyoung=검은 연주복(무대); dongmin=흰 반소매 남방·감색 반바지·빨간 손수건(본선); deoksu=단추를 목까지 잠근 체크 남방·빨간 손수건(본선); mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); bonggu=노란 반소매 남방·반바지·빨간 손수건(본선); yeongran=분홍 반소매 블라우스·감색 치마·빨간 손수건(본선); gyeongho=파란 티·반바지·빨간 손수건(본선); gyeongmin=주황 티·반바지·빨간 손수건(본선); suni=꽃무늬 원피스·빨간 손수건(본선); seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선); manseok=낡은 야전상의·다린 셔츠·운동화(본선); sunrye=외출용 자주색 블라우스·긴 치마, 접은 앞치마를 손에(본선); extra:객석=넥타이 신사, 부채 든 부인, 심사위원석; 학생 대부분은 사복(1980년대 국민학교 자유복, 중학교 교복은 학교마다 달랐음), 일부 사립학교 교복, 학부모는 1980년대 외출복; extra:엄마 한미숙(회상, 얼굴 금지)=회상 Insert — 근거 없음
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: `wall_close`(합판 벽과 손가락 마디 극접사(톡톡)) / 그 밖: `top_down`, `door_south`, `window_from_mat`, `section`
- 배경 `hanbit_hall` 한빛문화회관 홀 — 무대·객석 — 이 씬 카메라 자리: `house_back`(객석 뒤에서 무대 정면 와이드), `stage_to_house`(무대 위(은주 등 뒤 또는 은주 시점)에서 객석으로. 무대 옆은 화면 왼쪽), `center_seat`(객석 한가운데(만석) 가까이) / 그 밖: `floor_low`, `front_row_low`, `back_corner`
- 소품: `dongguri__s6_worn_e`(동그리(깡통 바이올린 1호)·본선 — E현이 닳음), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `can_violin_2__s1`(깡통 바이올린 2호(봉구)·완성(3-9 이후)), `can_violin_3__s1`(깡통 바이올린 3호(영란)·완성(3-9 이후)), `pot_lid_cymbals__s1`(냄비 뚜껑 심벌(경호·경민)·쌍둥이가 받은 그대로), `bottle_xylophone__s1`(병 실로폰(순이·석이)·물 높이를 맞춘 완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `newspaper_seoulmaeil__s3_flash`(신문 「한강신보」 사회면 단신·회상 극접사 — 단신 제목), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `plywood_wall`(합판 벽(판잣집 칸막이)), `glasses_seonyoung`(선영의 동그란 금테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `stage_curtain`(한빛문화회관 붉은 벨벳 커튼), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `manseok_field_jacket`(만석의 낡은 야전상의), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `concert_black`(검은 연주복(다솜중·선영))
- 소리 색 순간(이 컷들에만): 동민 뼈다귀 북 '톡톡' 빨강 #D9534A — 웃음소리가 싹 빠지는 컷, 북 가죽에서 아주 작은 빨간 동심원 두 번. 곡 시작 전 신호이므로 「섬의 하루」 누적 색 개수에는 넣지 않음

## 3-20 한빛문화회관 홀 — 무대·객석 (낮, 연속)
- 빛: 무대 위 따뜻한 호박빛 스포트(위·앞에서), 객석은 어둠 속 남색, 무대 나무 바닥에 따뜻한 반사. 겹침 Insert는 무대 위에 반투명으로: [새벽] 회청색 새벽, 둑길 트럭 불빛 / [아침] 뿌연 베이지 아침 빛, 고물 더미 / [한낮] 칠월 한낮 해, 쓰레기 산 꼭대기 바람
- 인물·의상: deoksu=단추를 목까지 잠근 체크 남방·빨간 손수건(본선); eunju=빌린 흰 원피스(무대); dongmin=흰 반소매 남방·감색 반바지·빨간 손수건(본선); mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); bonggu=노란 반소매 남방·반바지·빨간 손수건(본선); yeongran=분홍 반소매 블라우스·감색 치마·빨간 손수건(본선); gyeongho=파란 티·반바지·빨간 손수건(본선); gyeongmin=주황 티·반바지·빨간 손수건(본선); suni=꽃무늬 원피스·빨간 손수건(본선); seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선); seonyoung=검은 연주복(무대); choi=회색 양복·넥타이·서류 봉투; sunrye=외출용 자주색 블라우스·긴 치마, 접은 앞치마를 손에(본선); extra:객석=셋째 줄 어린아이와 엄마 등
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: 없음 / 그 밖: `top_south`, `slope_up`, `board_close`, `sky_low`
- 배경 `hanbit_hall` 한빛문화회관 홀 — 무대·객석 — 이 씬 카메라 자리: `floor_low`(무대 바닥 높이에서 객석 쪽으로 낮게 미끄러짐), `back_corner`(맨 뒷줄 왼쪽 구석(최 계장)) / 그 밖: `house_back`, `stage_to_house`, `front_row_low`, `center_seat`
- 배경 `scrap_heap` 큰 산 아래 쇳더미 — 이 씬 카메라 자리: 없음 / 그 밖: `heap_up`, `heap_pan`, `from_small_hill`
- 소품: `dongguri__s6_worn_e`(동그리(깡통 바이올린 1호)·본선 — E현이 닳음), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `can_violin_2__s1`(깡통 바이올린 2호(봉구)·완성(3-9 이후)), `can_violin_3__s1`(깡통 바이올린 3호(영란)·완성(3-9 이후)), `pot_lid_cymbals__s1`(냄비 뚜껑 심벌(경호·경민)·쌍둥이가 받은 그대로), `bottle_xylophone__s1`(병 실로폰(순이·석이)·물 높이를 맞춘 완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `choi_handkerchief__s2_damp`(최 계장의 손수건·땀에 젖은 손수건), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `scrap_sack`(고물 자루), `cotton_work_gloves`(목장갑), `red_rag_flag`(미자의 빨간 헝겊 깃발), `hanging_scale`(걸이 저울(고물상)), `choi_shoes`(최 계장의 반들반들한 구두), `glasses_seonyoung`(선영의 동그란 금테 안경), `glasses_choi`(최 계장의 검은 뿔테 안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `white_vinyl`(쓰레기 산의 흰 비닐 조각), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `concert_black`(검은 연주복(다솜중·선영)), `choi_gray_suit`(최 계장의 회색 양복), `dawn_truck`(새벽 첫 트럭(불빛))
- 소리 색 순간(이 컷들에만): [1. 새벽] 뚱보 주황 #E8944A — 1색. 기름통에서 낮은 물결 띠가 무대 바닥을 타고 객석으로 기어감(앞줄부터 웃음이 꺼지는 방향과 같이). 여기서 주변 채도 약 60% 낮춤 시작 / [2. 아침] + 동그리 금빛 #F5C04A(피치카토 '동, 동, 챙' — 짧은 점 같은 빛) → 2색, 이어 동민 북 '따닥-쿵' + 빨강 #D9534A → 3색. 주황은 옅은 띠로 남아 누적. 깡통 2·3호·냄비 뚜껑은 2절 표 밖이라 별도 색 없음 / [3. 한낮] + 꽥꽥이 청록 #4FB3A9 → 4색. 병 실로폰·아이들 웃음은 색 없음(표 밖). 네 색 띠가 바람을 따라 무대에서 천장으로 솟구침

## 3-21 한빛문화회관 홀 — 무대·객석 (낮, 연속)
- 빛: 무대 위 따뜻한 호박빛 스포트(위·앞에서), 객석은 어둠 속 남색, 무대 나무 바닥에 따뜻한 반사. 독주부터 조명이 좁아져 은주 하나만 스포트 안(나머지 무대도 어둠). 겹침: 해 질 녘 국밥집 천막(주황 잔광) / 라디오 수리점(세피아, 흐릿) / 노을 진 쓰레기 산 능선
- 인물·의상: eunju=빌린 흰 원피스(무대); deoksu=단추를 목까지 잠근 체크 남방·빨간 손수건(본선); mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); seonyoung=검은 연주복(무대); manseok=낡은 야전상의·다린 셔츠·운동화(본선); bonggu=노란 반소매 남방·반바지·빨간 손수건(본선); yeongran=분홍 반소매 블라우스·감색 치마·빨간 손수건(본선); gyeongho=파란 티·반바지·빨간 손수건(본선); gyeongmin=주황 티·반바지·빨간 손수건(본선); suni=꽃무늬 원피스·빨간 손수건(본선); seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선); extra:엄마 한미숙(회상, 얼굴 금지)=회상 겹침 — 근거 없음
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: 없음 / 그 밖: `top_south`, `slope_up`, `board_close`, `sky_low`
- 배경 `hanbit_hall` 한빛문화회관 홀 — 무대·객석 — 이 씬 카메라 자리: `center_seat`(객석 한가운데(만석) 가까이) / 그 밖: `house_back`, `stage_to_house`, `floor_low`, `front_row_low`, `back_corner`
- 배경 `hanbit_wing` 한빛문화회관 무대 옆, 커튼 뒤 — 이 씬 카메라 자리: `stage_to_wing`(무대 위에서 무대 옆 그늘로(은주 시점, 커튼 그늘의 영감)) / 그 밖: `wing_to_stage`, `curtain_gap_pov`, `steps_down`
- 배경 `fb_radio_shop` 회상: 1970년대 라디오 수리점 — 이 씬 카메라 자리: `bench_close`(작업대 위 손가락과 소리굽쇠(얼굴 없이))
- 소품: `dongguri__s7_e_broken`(동그리(깡통 바이올린 1호)·본선 — E현 끊김), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `tuning_fork_necklace__s0_mother`(은색 소리굽쇠 목걸이·회상 — 라디오 수리점에서 젊은 엄마의 손가락이 튕김), `sunrye_ladle__s2_borrowed`(순례 할머니의 국자·덕수가 빌려 간 국자(악기)), `soup_pot__s1`(국솥(국밥집 무쇠 솥)·김이 오르는 솥), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `soup_tent`(국밥집 천막), `glasses_seonyoung`(선영의 동그란 금테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `white_vinyl`(쓰레기 산의 흰 비닐 조각), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `manseok_field_jacket`(만석의 낡은 야전상의), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `concert_black`(검은 연주복(다솜중·선영)), `radio_repair_shop_radios`(회상: 라디오 수리점 선반의 라디오들)
- 소리 색 순간(이 컷들에만): [4. 저녁 시작] 국자 '탕, 탕, 탕' — 2절 표 밖, 새 색 없음. 누적 4색 유지 / [독주] 다른 색이 모두 물러나고 동그리 금빛 #F5C04A 하나만, 좁아진 스포트 안에서 가늘게(엄마 라디오 허밍 네 음) / [겹침 Insert] 라디오 수리점 소리굽쇠 '웅―' 은빛 흰색 #E9EEF5, 세피아 위에 흐릿하게 / [E현 끊김 '팅'] 금빛이 꺼진다 — 완전 무음 1초 동안 소리 색 0(채도 낮춘 화면 그대로, 빛 띠 없음) / [버팀] 뚱보 주황 #E8944A + 꽥꽥이 청록 #4FB3A9 두 색만, 끝나지 않는 저녁 바람처럼 길게 이어지는 띠

## 3-22 한빛문화회관 무대 옆, 커튼 뒤 (낮)
- 빛: 무대 옆 커튼 뒤 백열 작업등 하나(위, 노란 빛의 원), 커튼 틈으로 무대의 따뜻한 스포트가 한 줄 새어 듦, 나머지는 어둠. 커튼 틈으로 무대 쪽 빛이 깜박임
- 인물·의상: taejun=검은 연주복; eunju=빌린 흰 원피스(무대); kwak=다린 흰 반소매 셔츠·회색 바지(본선)
- 배경 `hanbit_wing` 한빛문화회관 무대 옆, 커튼 뒤 — 이 씬 카메라 자리: `wing_to_stage`(무대 옆 안쪽에서 무대 쪽으로: 왼쪽 커튼 틈, 의자와 작업등) / 그 밖: `curtain_gap_pov`, `stage_to_wing`, `steps_down`
- 소품: `dongguri__s7_e_broken`(동그리(깡통 바이올린 1호)·본선 — E현 끊김), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `taejun_violin__s1`(태준의 바이올린·변화 없음), `taejun_spare_e_string__s1_coiled`(태준의 여분 E현·동그랗게 감긴 새 줄(건넴)), `taejun_case`(태준의 고급 바이올린 케이스), `reading_glasses_kwak`(곽 영감의 돋보기안경), `hair_tie`(은주의 머리 고무줄), `stage_curtain`(한빛문화회관 붉은 벨벳 커튼), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `concert_black`(검은 연주복(다솜중·선영))
- 소리 색 순간(이 컷들에만): 소리굽쇠 '웅―' 은빛 흰색 #E9EEF5 — 은주가 무릎에 쳐서 울리는 '라' 한 음(대본: 무대 쪽 바람 소리 위로 라 한 음이 가늘게 떠오른다). 악기 색은 없음

## 3-23 한빛문화회관 홀 — 무대·객석 (낮)
- 빛: 무대 위 따뜻한 호박빛 스포트(위·앞에서), 객석은 어둠 속 남색, 무대 나무 바닥에 따뜻한 반사. 은주가 빠진 무대 가운데 스포트는 빈 채, 덕수·미자 쪽만 밝음(추정)
- 인물·의상: deoksu=단추를 목까지 잠근 체크 남방·빨간 손수건(본선); mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); choi=회색 양복·넥타이·서류 봉투; manseok=낡은 야전상의·다린 셔츠·운동화(본선)
- 배경 `hanbit_hall` 한빛문화회관 홀 — 무대·객석 — 이 씬 카메라 자리: `back_corner`(맨 뒷줄 왼쪽 구석(최 계장)), `center_seat`(객석 한가운데(만석) 가까이) / 그 밖: `house_back`, `stage_to_house`, `floor_low`, `front_row_low`
- 소품: `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `choi_handkerchief__s2_damp`(최 계장의 손수건·땀에 젖은 손수건), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `glasses_choi`(최 계장의 검은 뿔테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `manseok_field_jacket`(만석의 낡은 야전상의), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `choi_gray_suit`(최 계장의 회색 양복)
- 소리 색 순간(이 컷들에만): 뚱보 주황 #E8944A + 꽥꽥이 청록 #4FB3A9 — 두 색이 버팀(땀·볼 극접사 컷에도 띠 유지), 금빛 없음

## 3-24 한빛문화회관 무대 옆, 커튼 뒤 (낮)
- 빛: 무대 옆 커튼 뒤 백열 작업등 하나(위, 노란 빛의 원), 커튼 틈으로 무대의 따뜻한 스포트가 한 줄 새어 듦, 나머지는 어둠. 태준이 내려가는 컷: 무대 옆 계단에서 객석 어둠으로
- 인물·의상: kwak=다린 흰 반소매 셔츠·회색 바지(본선); taejun=검은 연주복; eunju=빌린 흰 원피스(무대)
- 배경 `hanbit_wing` 한빛문화회관 무대 옆, 커튼 뒤 — 이 씬 카메라 자리: `wing_to_stage`(무대 옆 안쪽에서 무대 쪽으로: 왼쪽 커튼 틈, 의자와 작업등), `steps_down`(무대 옆 계단에서 객석 어둠으로 내려감) / 그 밖: `curtain_gap_pov`, `stage_to_wing`
- 소품: `dongguri__s8_new_e`(동그리(깡통 바이올린 1호)·본선 — 태준의 새 E현으로 교체), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `taejun_violin__s1`(태준의 바이올린·변화 없음), `taejun_spare_e_string__s2_on_dongguri`(태준의 여분 E현·동그리에 걸린 새 E현), `taejun_case`(태준의 고급 바이올린 케이스), `reading_glasses_kwak`(곽 영감의 돋보기안경), `hair_tie`(은주의 머리 고무줄), `stage_curtain`(한빛문화회관 붉은 벨벳 커튼), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `concert_black`(검은 연주복(다솜중·선영))
- 소리 색 순간(이 컷들에만): 소리굽쇠 은빛 흰색 #E9EEF5 — '라와 미가 떨림 없이 맞물린다' 컷(대본: 주변 소리 빠지고 두 음만 남는다). 은빛 동심원 두 겹이 흔들리다 하나로 겹쳐 멎음. 악기 색은 없음

## 3-25 한빛문화회관 홀 — 무대·객석 (낮, 연속)
- 빛: 무대 위 따뜻한 호박빛 스포트(위·앞에서), 객석은 어둠 속 남색, 무대 나무 바닥에 따뜻한 반사. 겹침 몽타주: (1) 쓰레기 산 위의 별, 밤 남색 (2) 판잣집 창문의 노란 불빛 (3) 손전등을 들고 작은 산을 오르는 만석의 등, 손전등 원 하나
- 인물·의상: eunju=빌린 흰 원피스(무대); seonyoung=검은 연주복(무대); deoksu=단추를 목까지 잠근 체크 남방·빨간 손수건(본선); mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); dongmin=흰 반소매 남방·감색 반바지·빨간 손수건(본선); bonggu=노란 반소매 남방·반바지·빨간 손수건(본선); yeongran=분홍 반소매 블라우스·감색 치마·빨간 손수건(본선); gyeongho=파란 티·반바지·빨간 손수건(본선); gyeongmin=주황 티·반바지·빨간 손수건(본선); suni=꽃무늬 원피스·빨간 손수건(본선); seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선); taejun=검은 연주복; manseok=낡은 야전상의·다린 셔츠·운동화(본선); extra:객석=객석 전체
- 배경 `small_hill_top` 작은 산 꼭대기 — 이 씬 카메라 자리: 없음 / 그 밖: `top_south`, `slope_up`, `board_close`, `sky_low`
- 배경 `hanbit_hall` 한빛문화회관 홀 — 무대·객석 — 이 씬 카메라 자리: `house_back`(객석 뒤에서 무대 정면 와이드) / 그 밖: `stage_to_house`, `floor_low`, `front_row_low`, `back_corner`, `center_seat`
- 배경 `island_wide` 갈대섬 전경 — 이 씬 카메라 자리: `high_north`(뭍 쪽 하늘에서 섬 전체를 북향으로 내려다보는 높은 와이드)
- 배경 `shack_village` 판잣집 동네 외경 — 이 씬 카메라 자리: `roofs_to_entrance`(은주네 집 근처에서 지붕들 너머 남동쪽 섬 어귀(고물상 불빛 하나)) / 그 밖: `alley_west`
- 소품: `dongguri__s8_new_e`(동그리(깡통 바이올린 1호)·본선 — 태준의 새 E현으로 교체), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `bone_drum__s2_complete`(뼈다귀 북(X선 필름 북)·완성), `can_violin_2__s1`(깡통 바이올린 2호(봉구)·완성(3-9 이후)), `can_violin_3__s1`(깡통 바이올린 3호(영란)·완성(3-9 이후)), `pot_lid_cymbals__s1`(냄비 뚜껑 심벌(경호·경민)·쌍둥이가 받은 그대로), `bottle_xylophone__s1`(병 실로폰(순이·석이)·물 높이를 맞춘 완성), `baton__s1`(지휘봉(숟가락 자루 막대)·처음(1-14 받음)), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `sunrye_ladle__s2_borrowed`(순례 할머니의 국자·덕수가 빌려 간 국자(악기)), `taejun_spare_e_string__s2_on_dongguri`(태준의 여분 E현·동그리에 걸린 새 E현), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `drumstick_spoons`(북채(나무 숟가락 두 개)), `flashlight`(손전등), `glasses_seonyoung`(선영의 동그란 금테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `manseok_field_jacket`(만석의 낡은 야전상의), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `concert_black`(검은 연주복(다솜중·선영))
- 소리 색 순간(이 컷들에만): [5. 밤] 화면이 처음으로 온전히 색으로 찬다 — 뚱보 주황 #E8944A, 꽥꽥이 청록 #4FB3A9, 뼈다귀 북 빨강 #D9534A, 그리고 맨 위에 새 E현 금빛 #F5C04A(꺼졌던 금빛이 돌아옴, 가장 밝게). 이 씬부터 주변 채도 낮춤을 해제(본선 다섯 부분 중 유일) / [마지막 음] 금빛 동심원 하나가 홀 천장 조명 사이까지 올라가 머물다 사라짐

## 3-26 한빛문화회관 홀 — 무대·객석 (낮, 연속)
- 빛: 무대 위 따뜻한 호박빛 스포트(위·앞에서), 객석은 어둠 속 남색, 무대 나무 바닥에 따뜻한 반사. 기립 컷: 일어서는 객석은 무대 스포트의 반사광으로 앞줄부터 뒤로 따뜻하게 밝아짐(추정)
- 인물·의상: eunju=빌린 흰 원피스(무대); taejun=검은 연주복; sunrye=외출용 자주색 블라우스·긴 치마, 접은 앞치마를 손에(본선); extra:섬사람들=외출복(S#16); extra:객석=셋째 줄 아이와 엄마, 웃던 사람들; choi=회색 양복·넥타이·서류 봉투; manseok=낡은 야전상의·다린 셔츠·운동화(본선)
- 배경 `hanbit_hall` 한빛문화회관 홀 — 무대·객석 — 이 씬 카메라 자리: `house_back`(객석 뒤에서 무대 정면 와이드), `stage_to_house`(무대 위(은주 등 뒤 또는 은주 시점)에서 객석으로. 무대 옆은 화면 왼쪽), `front_row_low`(맨 앞줄 오른쪽 끝자리, 로앵글(태준 기립)), `back_corner`(맨 뒷줄 왼쪽 구석(최 계장)), `center_seat`(객석 한가운데(만석) 가까이) / 그 밖: `floor_low`
- 소품: `dongguri__s8_new_e`(동그리(깡통 바이올린 1호)·본선 — 태준의 새 E현으로 교체), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `choi_handkerchief__s2_damp`(최 계장의 손수건·땀에 젖은 손수건), `kwak_old_bow`(공장 시절 낡은 활(동그리의 활)), `handcart`(리어카), `glasses_choi`(최 계장의 검은 뿔테 안경), `work_cap_manseok`(만석의 국방색 작업모), `hair_tie`(은주의 머리 고무줄), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `manseok_field_jacket`(만석의 낡은 야전상의), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `concert_black`(검은 연주복(다솜중·선영)), `choi_gray_suit`(최 계장의 회색 양복)

## 3-27 한빛문화회관 홀 — 무대 (낮, 조금 뒤)
- 빛: 무대 위 따뜻한 호박빛 스포트(위·앞에서), 객석은 어둠 속 남색, 무대 나무 바닥에 따뜻한 반사. 시상이라 무대 위 전체가 고르게 밝음(따뜻한 스포트 그대로). 은주 시점 커튼 그늘(곽 영감): 무대 옆 커튼 뒤 백열 작업등 하나(위, 노란 빛의 원), 커튼 틈으로 무대의 따뜻한 스포트가 한 줄 새어 듦, 나머지는 어둠
- 인물·의상: eunju=빌린 흰 원피스(무대); seonyoung=검은 연주복(무대); dongmin=흰 반소매 남방·감색 반바지·빨간 손수건(본선); mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); deoksu=단추를 목까지 잠근 체크 남방·빨간 손수건(본선); bonggu=노란 반소매 남방·반바지·빨간 손수건(본선); yeongran=분홍 반소매 블라우스·감색 치마·빨간 손수건(본선); gyeongho=파란 티·반바지·빨간 손수건(본선); gyeongmin=주황 티·반바지·빨간 손수건(본선); suni=꽃무늬 원피스·빨간 손수건(본선); seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선); taejun=검은 연주복; extra:다솜중 단원=검은 연주복; kwak=다린 흰 반소매 셔츠·회색 바지(본선); extra:사회자·진행 요원=대본 근거 없음; extra:섬사람들=외출복(S#16)
- 배경 `hanbit_hall` 한빛문화회관 홀 — 무대·객석 — 이 씬 카메라 자리: `house_back`(객석 뒤에서 무대 정면 와이드) / 그 밖: `stage_to_house`, `floor_low`, `front_row_low`, `back_corner`, `center_seat`
- 배경 `hanbit_wing` 한빛문화회관 무대 옆, 커튼 뒤 — 이 씬 카메라 자리: `curtain_gap_pov`(커튼 틈 시점: 무대 위 연주(은주 시점)), `stage_to_wing`(무대 위에서 무대 옆 그늘로(은주 시점, 커튼 그늘의 영감)) / 그 밖: `wing_to_stage`, `steps_down`
- 소품: `dongguri__s8_new_e`(동그리(깡통 바이올린 1호)·본선 — 태준의 새 E현으로 교체), `ttungbo__s3_piano_wire`(뚱보(기름통 첼로)·피아노 쇠줄로 갈아 낀 뒤 + 국자 친 테두리), `kkwaekkwaegi__s2_fixed`(꽥꽥이(배수관 트럼펫)·수리 뒤(철사 한 바퀴 더 + 고무 조각)), `can_violin_2__s1`(깡통 바이올린 2호(봉구)·완성(3-9 이후)), `can_violin_3__s1`(깡통 바이올린 3호(영란)·완성(3-9 이후)), `pot_lid_cymbals__s1`(냄비 뚜껑 심벌(경호·경민)·쌍둥이가 받은 그대로), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `drumstick_spoons`(북채(나무 숟가락 두 개)), `glasses_seonyoung`(선영의 동그란 금테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `stage_curtain`(한빛문화회관 붉은 벨벳 커튼), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `mija_red_tracksuit`(미자의 빨간 트레이닝), `deoksu_check_shirt`(덕수의 체크 남방), `concert_black`(검은 연주복(다솜중·선영)), `result_envelope`(사회자의 결과 봉투), `microphone`(사회자 유선 마이크)

## 3-28 한빛문화회관 로비 (늦은 오후)
- 빛: 유리문으로 드는 늦은 오후의 낮은 햇빛(서쪽, 추정), 테라초 바닥 반사, 카메라 플래시의 순간 흰 섬광
- 인물·의상: eunju=빌린 흰 원피스(무대); taejun=검은 연주복; bonggu=노란 반소매 남방·반바지·빨간 손수건(본선); yeongran=분홍 반소매 블라우스·감색 치마·빨간 손수건(본선); gyeongho=파란 티·반바지·빨간 손수건(본선); gyeongmin=주황 티·반바지·빨간 손수건(본선); suni=꽃무늬 원피스·빨간 손수건(본선); seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자·빨간 손수건(본선)
- 배경 `hanbit_lobby` 한빛문화회관 로비 — 이 씬 카메라 자리: `lobby_glass`(홀 문 쪽에서 유리문 쪽으로(역광)), `two_shot_side`(사람들 사이 두 사람 옆모습 투숏)
- 소품: `dongguri__s8_new_e`(동그리(깡통 바이올린 1호)·본선 — 태준의 새 E현으로 교체), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `taejun_spare_e_string__s2_on_dongguri`(태준의 여분 E현·동그리에 걸린 새 E현), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `award_certificate__s1`(대상 상장·새 상장), `taejun_case`(태준의 고급 바이올린 케이스), `hair_tie`(은주의 머리 고무줄), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `concert_black`(검은 연주복(다솜중·선영)), `bouquet`(꽃다발), `camera_flash`(사진기(플래시))

## 3-29 한빛문화회관 앞 계단 (저녁, 해 질 녘)
- 빛: 해 질 녘 낮은 해, 광장 쪽(만석 뒤)에서 — 만석의 그림자가 계단 위까지 길게, 주황 금빛 역광
- 인물·의상: manseok=낡은 야전상의·다린 셔츠·운동화(본선); eunju=빌린 흰 원피스(무대); sunrye=외출용 자주색 블라우스·긴 치마, 접은 앞치마를 손에(본선); choi=회색 양복·넥타이·서류 봉투; mija=새것 같은 빨간 트레이닝 위아래·빨간 손수건(본선); extra:섬사람들=외출복(S#16)
- 배경 `hanbit_front` 한빛문화회관 앞·계단 — 이 씬 카메라 자리: `steps_down`(계단 위에서 광장 쪽으로 내려다봄(긴 그림자, 역광)), `plaza_wide`(광장의 전세 버스와 사람들, 노을 와이드) / 그 밖: `steps_up`
- 소품: `dongguri__s8_new_e`(동그리(깡통 바이올린 1호)·본선 — 태준의 새 E현으로 교체), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `pawn_ticket_manseok__s1`(만석의 전당표·닳은 전당표), `choi_handkerchief__s1_dry`(최 계장의 손수건·마른 손수건), `sunrye_ladle__s1`(순례 할머니의 국자·할머니 손의 국자), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `choi_envelope`(최 계장의 누런 서류 봉투), `charter_bus`(낡은 전세 버스), `glasses_choi`(최 계장의 검은 뿔테 안경), `work_cap_manseok`(만석의 국방색 작업모), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `borrowed_white_dress`(선영이 빌려 온 흰 원피스), `manseok_field_jacket`(만석의 낡은 야전상의), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `mija_red_tracksuit`(미자의 빨간 트레이닝), `choi_gray_suit`(최 계장의 회색 양복)

## 3-30 둑길 (저녁, 노을)
- 빛: 노을, 낮은 해는 강 쪽(서쪽, 추정), 하늘 주황 → 보라 그러데이션, 판잣집 지붕 위 저녁연기, 큰 산·작은 산은 실루엣
- 인물·의상: eunju=빌린 흰 원피스(무대); dongmin=흰 반소매 남방·감색 반바지·빨간 손수건(본선)
- 배경 `dyke_road_to_island` 둑길 — 뭍 쪽에서 섬을 봄(같은 구도 기준) — 이 씬 카메라 자리: `mainland_north_fixed`(뭍 쪽 끝에서 섬 쪽으로(북향) 고정 와이드 — 3-30·3-31·3-32 '같은 구도' 기준)
- 소품: `dongguri__s8_new_e`(동그리(깡통 바이올린 1호)·본선 — 태준의 새 E현으로 교체), `tuning_fork_necklace__s4_rehung`(은색 소리굽쇠 목걸이·만석이 다시 걸어 줌 — 쇄골 위), `red_neckerchief__s2_tied`(빨간 손수건(본선 목 스카프)·목에 맨 모습), `charter_bus`(낡은 전세 버스), `bandage`(반창고(미자 코·동민 무릎)), `hair_tie`(은주의 머리 고무줄), `borrowed_white_dress`(선영이 빌려 온 흰 원피스)

## 3-31 푸른 언덕 공원 (낮, 2003년 봄)
- 빛: 봄 한낮 맑은 햇빛(위·왼쪽), 처음으로 뿌옇지 않은 맑은 파란 하늘, 화면 전체 자연색으로 밝음
- 인물·의상: 
- 배경 `park_2003_view` 푸른 언덕 공원(2003) — 같은 구도 — 이 씬 카메라 자리: `mainland_north_fixed`(dyke_road_to_island와 같은 자리·같은 구도(북향))
- 소품: `park_banner_slope`(언덕 비탈 현수막(2003))

## 3-32 몽타주 — 섬이 언덕이 되기까지 (1988년 가을 ~ 2003년)
- 빛: (1) 1988 가을 둑길: 맑은 가을 오전, 뿌연 베이지 하늘 / (2~3) 임시 거처 골목(1988): 가을 낮, 부드러운 빛 → 디졸브 임대주택 골목(1990): 낮, 맑은 빛 / (4) 학교 교문: 가을 아침 햇빛 / (5) 빈 섬: 흐린 낮, 회갈 / (6) 흙 덮임: 흐린 낮, 흙빛 / (7) 첫 싹: 같은 구도, 빛이 계절마다 바뀜 / (8) 푸른 언덕: 2003 봄 맑은 한낮
- 인물·의상: extra:섬사람들=대본 근거 없음 — 섬사람 평상복(가을); sunrye=몸뻬 바지·꽃무늬 앞치마; choi=회색 양복·넥타이·서류 봉투; dongmin=물려받은 큰 운동복; deoksu=늘어난 흰 러닝셔츠 위 체크 남방; extra:섬 아이들(봉구·영란·경호·경민·순이·석이)=섬 아이들 평상복(가을)
- 배경 `dyke_road` 둑길·섬 어귀 — 섬 쪽에서 뭍을 봄 — 이 씬 카메라 자리: 없음 / 그 밖: `island_end_south`, `bank_side`, `middle_wide`, `low_shoes`
- 배경 `dyke_road_to_island` 둑길 — 뭍 쪽에서 섬을 봄(같은 구도 기준) — 이 씬 카메라 자리: `mainland_north_fixed`(뭍 쪽 끝에서 섬 쪽으로(북향) 고정 와이드 — 3-30·3-31·3-32 '같은 구도' 기준)
- 배경 `park_2003_view` 푸른 언덕 공원(2003) — 같은 구도 — 이 씬 카메라 자리: `mainland_north_fixed`(dyke_road_to_island와 같은 자리·같은 구도(북향))
- 배경 `island_after` 갈대섬 전경(매립 끝난 뒤, 1990년대) — 이 씬 카메라 자리: `mainland_north_fixed`(dyke_road_to_island와 같은 자리·같은 구도(북향))
- 배경 `temp_alley` 임시 거처 골목 (1988) — 이 씬 카메라 자리: `entrance_in`(골목 입구에서 안으로(입구에 서류 든 최 계장))
- 배경 `rental_alley` 임대주택 골목 — 이 씬 카메라 자리: `entrance_in`(골목 입구에서 안으로(입구에 서류 든 최 계장))
- 배경 `school_gate` 학교 교문 — 이 씬 카메라 자리: `street_in`(길에서 교문 안으로 뛰어 들어가는 아이들)
- 소품: `choi_handkerchief__s1_dry`(최 계장의 손수건·마른 손수건), `choi_envelope`(최 계장의 누런 서류 봉투), `glasses_choi`(최 계장의 검은 뿔테 안경), `bandage`(반창고(미자 코·동민 무릎)), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `deoksu_check_shirt`(덕수의 체크 남방), `dongmin_tracksuit`(동민의 물려받은 큰 운동복), `choi_gray_suit`(최 계장의 회색 양복), `moving_trucks`(이삿짐 실은 트럭들), `relocation_list`(이주 명단), `earth_dozer`(흙 덮는 장비)

## 3-33 회상 — 만복전당포 (1988년 여름, 낮)
- 빛: 누런 형광등(위), 문이 열릴 때 바깥 여름 낮 빛이 한 줄
- 인물·의상: mija=빨간 반소매 티(여름); bonggu=노란 러닝셔츠·반바지; yeongran=분홍 반소매 블라우스·감색 치마; gyeongho=파란 티·반바지; gyeongmin=주황 티·반바지; suni=꽃무늬 원피스; seoki=물려받은 큰 반소매 티(소매가 팔꿈치 아래로)·큰 모자; extra:전당포 주인=대본 근거 없음
- 배경 `pawnshop` 만복전당포 — 이 씬 카메라 자리: `door_in`(문 안에서 계산대 쪽으로(진열장 왼쪽)), `counter_top`(계산대 위 부감(케이스 안, 전당표, 동전)) / 그 밖: `counter_reverse`
- 소품: `manseok_clarinet__s2_pawned_case`(만석의 클라리넷·전당포 창고 — 먼지 쌓인 클라리넷 케이스), `mija_savings_can__s2_full`(미자의 '찾을 돈' 깡통·가득 — 계산대 위로 뒤집음(3-33)), `scrap_money`(고물값 지폐·동전), `door_bell`(전당포 문 위의 종), `abacus`(주판), `bandage`(반창고(미자 코·동민 무릎)), `pawnshop_showcase`(전당포 유리 진열장과 계산대), `pawned_violin_case`(전당포 창고의 바이올린 케이스(선영의 바이올린))

## 3-34 푸른 언덕 공원 꼭대기, 작은 무대 (낮, 2003년 봄)
- 빛: 봄 한낮, 하늘을 넓게, 해는 위·뒤쪽(추정) — 무대에 짙은 그늘 없음, 언덕 아래 강물 반짝임. 화면 전체 자연색으로 밝음. 회상 Insert(쪽방, 소리 없이): 1987년 밤 남색
- 인물·의상: eunju=짙은 남색 연주 드레스(2003, 어른); manseok=다린 흰 셔츠·검은 바지(2003, 백발); kwak=깨끗한 갈색 카디건(2003); seonyoung=단정한 감색 정장(2003, 음악 교사); mija=감색 트레이닝복·호루라기·출석부(2003, 체육 교사); deoksu=꽃무늬 앞치마(2003, 국밥집); dongmin=검은 티셔츠·청바지(2003, 어른); taejun=검은 정장 연주복(2003, 어른); choi=넥타이 없는 회색 양복(2003); sunrye=자주색 외출 블라우스·긴 치마(2003, 객석); extra:선영의 학생들=교복(대본); dongmin=물려받은 큰 운동복
- 배경 `shack_side` 은주네 판잣집 — 쪽방 — 이 씬 카메라 자리: 없음 / 그 밖: `top_down`, `door_south`, `window_from_mat`, `wall_close`, `section`
- 배경 `park_2003_stage` 푸른 언덕 공원 꼭대기, 작은 무대(2003) — 이 씬 카메라 자리: `audience_back`(객석 뒤에서 무대와 하늘을 넓게(남향)), `stage_to_audience`(무대에서 객석으로(은주 시점, 맨 앞줄부터 팬, 북향)), `down_slope`(언덕 비탈을 따라 강 쪽으로 내려감(풀밭과 흙))
- 소품: `dongguri__s9_epilogue`(동그리(깡통 바이올린 1호)·15년 뒤(2003 봄, 에필로그)), `tuning_fork_necklace__s5_epilogue`(은색 소리굽쇠 목걸이·15년 뒤(2003)), `mother_radio__s2_epilogue`(엄마의 고장 난 트랜지스터라디오·15년 뒤 — 의자 위, 허밍이 새어 나옴(2003)), `manseok_clarinet__s3_epilogue`(만석의 클라리넷·15년 뒤 — 새로 맞춘 패드, 반들반들한 키(2003)), `choi_handkerchief__s1_dry`(최 계장의 손수건·마른 손수건), `blanket`(이불), `kwak_pencil`(곽 영감이 귀에 꽂은 연필), `glasses_seonyoung`(선영의 동그란 금테 안경), `glasses_choi`(최 계장의 검은 뿔테 안경), `reading_glasses_kwak`(곽 영감의 돋보기안경), `hair_tie`(은주의 머리 고무줄), `folding_chair`(접이식 의자), `sunrye_apron`(순례 할머니의 꽃무늬 앞치마), `choi_gray_suit`(최 계장의 회색 양복), `concert_banner`(작은 무대 현수막(2003)), `small_wooden_stage`(언덕 꼭대기 작은 나무 무대(2003)), `eunju_real_violin_case`(어른 은주의 진짜 바이올린 케이스(꼬리표)), `whistle_rollbook`(미자의 호루라기·출석부(2003)), `deoksu_big_pot`(덕수의 큰 냄비(2003)), `dongmin_drumsticks_2003`(어른 동민의 북채(2003))
- 소리 색 순간(이 컷들에만): 엄마의 라디오 허밍 연보라 #B9A7D9 — 마지막, '주변 소리 모두 빠지고 라디오의 허밍만 남는다' 컷. 라디오 스피커에서 가는 연보라 동심원만 퍼지고, 주변 채도는 낮추지 않음(에필로그: 화면 전체 자연색으로 밝음)
