# zwcad_control.py

def draw_from_excel_mock(df):
    print("📐 [모의 실행] CAD 명령어 전개 시작")

    for idx, row in df.iterrows():
        try:
            distance = row["누가거리"]
            ground = row["지반고"]
            invert = row["관저고"]
            manhole = row["맨홀"]

            print(f"→ 누가거리: {distance}, 지반고: {ground}, 관저고: {invert}, 맨홀: {manhole}")
        except Exception as e:
            print(f"⚠️ 데이터 오류 발생: {e}")
