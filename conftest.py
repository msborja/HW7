import pytest
import os.path
import zipfile
import shutil

RESOURCES_PATH = os.path.join(os.getcwd(), "resources")
ZIPPED_PATH = os.path.join(os.getcwd(), "zipped_resources")
ZIPPED_RESOURCES = os.path.join(os.getcwd(), 'zipped_resources', 'zipped_resources.zip')


# Создаем архив archive.zip и кладём туда файлы PDFfile.pdf', 'XLSXfile.xlsx', 'CSVfile.csv
@pytest.fixture(scope='function', autouse=True)
def create_archive():
    if not os.path.exists(ZIPPED_PATH):
        os.mkdir(ZIPPED_PATH)
    with zipfile.ZipFile(ZIPPED_PATH + '/zipped_resources.zip', 'w') as zf:
        for file in os.listdir(RESOURCES_PATH):
            add_file = os.path.join(RESOURCES_PATH, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree(ZIPPED_PATH)
