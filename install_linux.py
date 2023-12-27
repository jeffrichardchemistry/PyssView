
import os
import shutil

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))

class Install:
    def __init__(self):
        self.local_path = '{}/.local/share/applications/PyssView.desktop'.format(os.path.expanduser('~'))       
        Install.main(self) 
    
    def main(self):       
        #get directory to install
        dir2install = Install.getDir2install(self)
        
        #Copy and extract binary app
        Install.copyExtractTar(self, dir2install)
        
        #Make Desktop shortcut and Icon
        Install.makeDesktopFile(self,
                                exec_path='{}/pyssview/pyssview'.format(dir2install),
                                icon_path='{}/pyssview/_internal/icons/logo3.svg'.format(dir2install))
        
    def makeDesktopFile(self, exec_path, icon_path):
        desktop = """
[Desktop Entry]
Name=PyssView
GenericName=PyssView
Comment=Account organize
Exec={}
Terminal=false
Type=Application
Icon={}
StartupNotify=false
Categories=Network;
        """.format(exec_path, icon_path)        
        
        with open(self.local_path, 'w') as deskfile:
            deskfile.write(desktop)
        
    def getDir2install(self):
        while True:
            dir2install = str(input('Type a directory to install [Default:{}]: '.format(os.path.expanduser('~'))))
            if os.path.isdir(dir2install):
                if dir2install[-1] == '/':
                    return dir2install[:-1]
                else:
                    return dir2install
            elif dir2install == '':
                return os.path.expanduser('~')               
            else:
                print('Invalid directory. Installing in {}\n'.format(os.path.expanduser('~')))
                return os.path.expanduser('~')
    
    def copyExtractTar(self, dirinstall):
        print('Copying files...')
        shutil.copy('{}/bin/PyssView.tgz'.format(ABSOLUT_PATH), 
                    dirinstall)
        print('Copying files Finished.\nExtracting tgz...')
        shutil.unpack_archive('{}/PyssView.tgz'.format(dirinstall),
                              dirinstall,
                              'tar'
                              )
        print('Extraction Finished.')
        os.remove('{}/PyssView.tgz'.format(dirinstall))
        
        
install_run = Install()
    
    
