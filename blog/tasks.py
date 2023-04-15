# Create your tasks here

from blog.models import *
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from celery import shared_task


@shared_task
def verify(email):
    
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








@shared_task
def verified(link):
    sub = Subscribers.objects.get(id=link)
    sub.is_verified = True
    sub.save()
















@shared_task
def notify():
    head = """
                               
                        <!doctype html>
                        <html lang="en-US">

                        <head>
                          <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
                          <title>Notifications Email Template</title>
                          <meta name="description" content="Notifications Email Template">
                          <style >
                              
                        .trunc{
                          display: -webkit-box;
                          -webkit-line-clamp: 7;
                          -webkit-box-orient: vertical;
                          width: auto;
                          overflow: hidden;
                        }

                          </style>
                        </head>

                        <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" bgcolor="#eaeeef"
                          leftmargin="0">
                          <!--100% body table-->
                          <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
                            style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
                            <tr>
                              <td>
                                <table style="background-color: #f2f3f8; max-width:670px; margin:0 auto;" width="100%" border="0" align="center"
                                  cellpadding="0" cellspacing="0">
                                  <tr>
                                    <td style="height:80px;">&nbsp;</td>
                                  </tr>
                                  <tr>
                                    <td style="text-align:center;">
                                      <a href="#" title="logo">
                                        <img width="210" src="assets/images/logo.png" title="logo" alt="logo">
                                      </a>
                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="40px;">&nbsp;</td>
                                  </tr>
                                  <tr>
                                    <td>
                                      <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                        style="max-width:600px; background:#fff; border-radius:3px; text-align:left;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                        <tr>
                                          <td style="padding:40px;">
                                            <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                                              <tr>
                                                <td>
                                                  <h1 style="color: #1e1e2d; font-weight: 500; margin: 0; font-size: 32px;font-family:'Rubik',sans-serif;">Hi Jhon,</h1>
                                                  <p style="font-size:15px; color:#455056; line-height:24px; margin:8px 0 30px;">Here's a list
                                                    of activities which needs your attention.</p>
                                                </td>
                                              </tr>
                                              <tr>
                                                <td>
                                                  <table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                            

                                              """

    for i in Subscribers.objects.all():
        email = i.mail
        int1 = i.intrest1
        int2 = i.intrest2
        int3 = i.intrest3
        uuid = Subscribers.objects.get(mail=email).id
            
        link = 'http://127.0.0.1:8000/email-varification/'+str(uuid)
        foot = f"""
                                        </table>


                                                      </td>
                                                     
                                                    </tr>
                                                  </table>
                                                 <p><a href="{link}" >Click here</a> to Change your intrest</p>  
                                                </td>
                                              </tr>
                                            </table>
                                          </td>
                                        </tr>
                                        
                                        <tr>
                                          <td style="height:25px;">&nbsp;</td>
                                        </tr>
                                        
                                        <tr>
                                          <td style="text-align:center;">
                                              <p style="font-size:14px; color:#455056bd; line-height:18px; margin:0 0 0;">Credit <strong>text goes here</strong></p>
                                          </td>
                                        </tr>
                                        <tr>
                                          <td style="height:80px;">&nbsp;</td>
                                        </tr>
                                      </table>
                                    </td>
                                  </tr>
                                </table>
                                <!--/100% body table-->
                              </body>

                              </html>
                                            """


        
        
        blog = Blog.objects.filter(Q(heading__icontains = int1)|Q(header__contains = int1)|Q(heading__icontains = int2)|Q(header__contains = int2)|Q(heading__icontains = int3)|Q(header__contains = int3))
        body = ""
        for i in blog:
            
            content = f"""
                                
                                                    <tr
                              style="border-bottom:1px solid #ebebeb; margin-bottom:26px; padding-bottom:29px; display:block;">
                              <td width="auto">
                              </td>
                              <td style="vertical-align:top;">
                              <a href="http://127.0.0.1:8000/{i.category.slug}/{i.slug}/">
                                <h3 style="color: #4d4d4d; font-size: 20px; font-weight: 400; line-height: 30px; margin-bottom: 3px; margin-top:0;">
                                    <strong>{i.heading}</strong></h3></a>
                                <span style="color:#737373; font-size:14px;">{i.date} {i.timetoread} Minutes reading</span> <br>
                                <p class="trunc" style="font-size:14px;" >{i.header}</p>
                              </td>
                            </tr>
                                                            

                                        
                        """
            
            body += content 
          
        subject = "New Contents are Arrived!!!"
        bodys = head + body + foot
        from_email = 'support.careerenv.com'
        to = [email,]

        mail = EmailMultiAlternatives(subject,bodys,from_email,to)
            #mail.attach_alternative(, "text/html")

            #html = get_template("email_varify.html").render()
        mail.attach_alternative(bodys, "text/html")
        mail.send()