# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'MyQR',
    version = '3.0.0',
    keywords = ('qr', 'qrcode', 'qr code', 'artistic', 'animated', 'gif'),
    description = 'Generater for amazing QR Codes. Including Common, Artistic and Animated QR Codes.',
    long_description = '''
        Home Page: https://github.com/Isvvc/qrcode
    
        Overview
        ===============
        It can generate common qr-code, artistic qr-code (black & white or colorized), animated qr-code (black & white or colorized).

        Usage
        ===============
        terminal:
        
        myqr input_filename
             [-h]
             [-v {1,2,3,...,40}]
             [-l {L, M, Q, H}]
             [-p image_filename]
             [-c]
             [-con contrast_value]
             [-bri brightness_value]
             [-n output_filename]
             [-d output_directory]

             
        import:
         
        from MyQR import myqr
        version, level, qr_name = myqr.run(
            words,
            version = 1,
            level = 'H',
            picture = None,
            colorized = False,
            contrast = 1.0,
            brightness = 1.0,
            save_name = None,
            save_dir = os.getcwd()
            )
             
             
        More
        ===============
        Please visit 'Home Page' for examples and details.
        
        Updates
        ===============
        version 3.0.0 - Read input from file.
        version 2.3.1 - Fixed another bug of number encoding.
        version 2.2.1 - Fixed a bug of number encoding.
        version 2.1.1 - Fixed a characters support problem.
        version 2.0.1 - Improved structure.
        version 2.0.0 - Recoded to be importable.
        version 1.0.0 - Distributed to PyPI.
        
        
        
        
    ''',

    author = 'Isvvc',
    author_email = 'lyons@tuta.io',
    url = 'https://github.com/Isvvc/qrcode',
    download_url = 'https://github.com/Isvvc/qrcode',

    install_requires = [
        'imageio >= 1.5',
        'numpy >= 1.11.1',
        'Pillow>=3.3.1'
    ],
    packages = ['MyQR', 'MyQR.mylibs'],
    
    license = 'GPLv3',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    entry_points = {
        'console_scripts': [
            'myqr = MyQR.terminal:main',
        ],
    }
)
