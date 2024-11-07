import os
import pandas as pd

def list_files_in_directory(directory, output_file):
    data = []
    file_number = 1  # 파일 순번 초기화
    
    for root, dirs, files in os.walk(directory):
        # 현재 디렉토리의 파일들 처리
        parent_folder = os.path.basename(root)
        
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):  # 파일일 때만 처리
                data.append([file_number, parent_folder, file_name])  # 순번, 상위 폴더 이름, 파일 추가
                file_number += 1  # 파일 순번 증가
    
    # DataFrame으로 변환
    df = pd.DataFrame(data, columns=["File Number", "Parent Folder", "File"])
    
    # 엑셀 파일로 저장
    df.to_excel(output_file, index=False)

# 사용 예시:

directory_path = "C:/Users/user/Desktop/교육생 라벨링/현수막 라벨링"  # 원하는 폴더 경로
output_excel = "C:/Users/user/Desktop/교육생 라벨링/교육생현수막다운로드_1028_2.xlsx"  # 저장할 엑셀 파일 이름

list_files_in_directory(directory_path, output_excel)

print(f"폴더 내의 파일 목록이 {output_excel}에 저장되었습니다.")
