import os
import pandas as pd

#C:\Users\user\Desktop\작업폴더\632_660_20240912\632\편집

def list_files_in_edit_folder(directory, output_file):
    data = []
    file_number = 1  # 파일 순번 초기화
    
    for root, dirs, files in os.walk(directory):
        # '편집' 폴더가 있을 때만 그 폴더 안의 파일을 처리
        if '편집' in dirs:
            edit_folder_path = os.path.join(root, '편집')  # '편집' 폴더 경로 생성
            
            # '편집' 폴더의 상위 폴더 이름 추출 (예: '632')
            parent_folder = os.path.basename(root)
            
            # '편집' 폴더 안의 파일들만 추출
            for file_name in os.listdir(edit_folder_path):
                file_path = os.path.join(edit_folder_path, file_name)
                if os.path.isfile(file_path) and file_name != 'Thumbs.db':  # 파일일 때만 처리하고 Thumbs.db 제외
                    data.append([file_number, parent_folder, file_name])  # 순번, 상위 폴더 이름, 파일 추가
                    file_number += 1  # 파일 순번 증가
            
            file_number=1
    
    # DataFrame으로 변환
    df = pd.DataFrame(data, columns=["File Number", "Parent Folder", "File"])
    
    # 엑셀 파일로 저장
    df.to_excel(output_file, index=False)

# 사용 예시: 

directory_path = "C:/Users/user/Desktop/작업폴더/632_660_20240912"  # 원하는 폴더 경로
output_excel = "C:/Users/user/Desktop/작업폴더/632_660_20240912/632_660_20240912_list.xlsx"  # 저장할 엑셀 파일 이름

list_files_in_edit_folder(directory_path, output_excel)

print(f"폴더 내의 파일 목록이 {output_excel}에 저장되었습니다.")
