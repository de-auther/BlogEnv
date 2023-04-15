import asyncio
from asgiref.sync import sync_to_async

@sync_to_async  
def test(email):
    
    user = Subscribers(mail = email)
    user.save()
    uuid = Subscribers.objects.get(mail=email).id
            
    link = 'http://127.0.0.1:8000/email-varification/'+str(uuid)
            



    subject='E-Mail Verification'
    body= """
            
                        <!DOCTYPE html>
                        <html>
                        <head> <title></title> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1"> <meta http-equiv="X-UA-Compatible" content="IE=edge" /> 
                        </head>
                        <body style="background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;">
                        </head> <table border="0" cellpadding="0" cellspacing="0" width="100%"> <!-- LOGO --> <tr> <td bgcolor="#f4f4f4" align="center"> <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;"> <tr> <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td> </tr> </table> </td> </tr> <tr> <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;"> <tr> <td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 2px 2px 0px 0px; color: #AADB1E; font-family: 'Londrina Solid'Helvetica, Arial, sans-serif; font-size: 45px; font-weight: 700; letter-spacing: 2px; line-height: 48px;"> <h1 style="font-size: 40px; font-weight:700; margin: w-50;"><img style="border-radius: 100%; height: 50px; width: 50px; " src="https://careerenv.pythonanywhere.com/static/logo.png" alt=""> CAREERENV</h1> </td> </tr> </table> </td> </tr> <tr> <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;"> <tr> <td bgcolor="#ffffff" align="center" style="padding: 20px 30px 40px 30px; color: #000000; font-family:'Montserrat bold' Helvetica, Arial, sans-serif; font-size: 16px; font-weight:600; line-height: 25px;"> <p >Kindly verify and select your email and add your interest to complete your newsletter subsciption.</p> </td> </tr> <tr> <td bgcolor="#ffffff" align="left"> <table width="100%" border="0" cellspacing="0" cellpadding="0"> <tr> <td bgcolor="#ffffff" align="center" style="padding: 20px 30px 60px 30px;"> <table border="0" cellspacing="0" cellpadding="0"> <tr> <td align="center" style="border-radius: 30px;" bgcolor="#000000"><a href="{links}" target="_blank" style="font-size: 20px; font-family: 'Montserrat Bold'Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 10px 55px; border-radius: 2px; display: inline-block;">VERIFY NOW</a></td> </tr> </table> </td> </tr> </table> </td> </tr> <!-- COPY --> <tr> <td bgcolor="#ffffff" align="center" style="padding: 0px 30px 0px 30px; color: #000000; font-family:'Montserrat'Helvetica, Arial, sans-serif; font-size: 14px; font-weight:550; line-height: 25px;"> <p style="margin: 0;">Alternatively, you can copy this URL to your browser:</p> </td> </tr> <!-- COPY --> <tr> <td bgcolor="#ffffff" align="center" style="padding: 20px 30px 20px 30px; color: #666666; font-family:'Montserrat'Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 550; line-height: 25px;"> <p style="margin: 0;"><a href="{links}" target="_blank" style="color: #29ABE2;">{links}</a></p> </td> </tr> <tr> <td bgcolor="#ffffff" align="center" style="padding: 0px 30px 20px 30px; color: #000000; font-family:'Montserrat'Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 25px;"> <p style="margin: 0;">The link will be valid for the next 24 hours.</p> </td> </tr> <tr> <td bgcolor="#ffffff" align="center" style="padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #000000; font-family:'Montserrat'Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 25px;"> <p style="margin: 0;">Contact us at <a href="#" target="_blank" style="color: #29ABE2;">support@careerenv.com</a></p> </td> </tr> <!-- <tr> <td bgcolor="#ffffff" align="center" style="padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #333333; font-family:'Montserrat'Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 25px;"> <img src="https://img.icons8.com/ios-glyphs/30/000000/facebook-new.png"/> <img src="https://img.icons8.com/material-outlined/30/000000/instagram-new.png"/> </td> </tr> --> </table> </td> </tr> <tr> <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;"> <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;"> <tr> <td bgcolor="#f4f4f4" align="center" style="padding: 0px 30px 30px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 18px;"> <br> <p style="margin: ;"><a href="#" target="_blank" style="color: #111111; font-weight: 700;"</p> </td> </tr> </table> </td> </tr> </table>
                        </body>
                        </html>
                        
                        
                    """
    test = body.format(links=link)
    from_email = 'support.careerenv.com'
    to = [email,]

    mail = EmailMultiAlternatives(subject,body,from_email,to)
            #mail.attach_alternative(, "text/html")

            #html = get_template("email_varify.html").render()
    mail.attach_alternative(test, "text/html")
    mail.send()
    return "Done"
    