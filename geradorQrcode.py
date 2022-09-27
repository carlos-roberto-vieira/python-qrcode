import qrcode 
img  =  qrcode.make( 'www.tssistemas.com' ) 
img.save ( "qrcode.png" )