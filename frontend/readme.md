# GoBlog

## install packages , setup, & buat Avatar

    Todo:
    1.  Install axios ,bootstrap, dn react-router-dom
     cd frontend : npm i axios react-router-dom bootstrap
    2.  src/main.js
        - pasang bootstrap
    3.  src/App.js
        - pasang react-router-dom
        - panggil Home sebagai route
    4.  src/assets/images
        - masukan gambar avatar
    5.  src/components/Avatar.jsx
        - buat functional Avatar component
        - buat props & pasang {height,width,...rest}, yang nanti akan dipanggil.
          props dibuat agar membuat flexible pada kegunaannya
    6.  src/pages/Home.jsx
        - buat functional Home component
        - import dan panggil Avatar, kemudian pasang props height & src
        - import dan panggil Image
    7.  pengujian pada browser:
        http://localhost:5173

## CardProfile components

    Todo:

    1.  src/components/Avatar.jsx
        - buat functional CardProfile component
        - import dan panggil Avatar
    2.  src/pages/Home.jsx
        - import dan pasang CardProfile
    3.  pengujian pada browser:
        http://localhost:5173

## Modal & Button components

    Todo:

    1.  src/components/Button.jsx
        - buat functional Button component
        - pasang props label, variant , {...rest}
    2.  src/components/Modal.jsx
        - buat functional Modal component
        - buat modal dari bootstrap modal
        - import dan pasang Button: pasang button pada modal
    3.  src/pages/Home.jsx
        - import dan pasang Modal component
    4.  pengujian pada browser:
        http://localhost:5173

## Login Page

    Todo:

    1.  src/components/Input.jsx
        - buat functional Input component
        - pasang props label, {...rest}
    2.  src/components/Gap.jsx
        - buat functional Gap component
        - pasang props height, width pada style
    3.  src/pages/Login.jsx
        - buat functional Login component
        - import & pasang Button
        - import & pasang Input
        - import & pasang Gap
    4.  App.js
        - import dan pasang Login pada path element
    5.  pengujian pada browser:
        http://localhost:5173/login

    6.  Noted : Gap dibuat untuk memberi jarak pada setiap component

## Register Page

    Todo:

    1.  Duplicate Login Page
        - kemudin modifikasi
    2.  pengujian pada browser:
        http://localhost:5173/register
