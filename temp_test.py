import os
import shutil
import zipfile

if __name__ == '__main__':
    ex_file = r'F:\quhong\DEMO\www\eid_sheep.png'
    new_f_path = 'thumb.png'
    UPLOAD_FOLDER = ''
    new_f_path = os.path.join(os.path.dirname(ex_file), new_f_path)
    shutil.copy(ex_file, new_f_path)

    zip_filename = os.path.join(os.path.dirname(ex_file), 'eid_sheep' + '.zip')
    zip = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
    zip.write(new_f_path, arcname='thumb.png')
    zip.close()

