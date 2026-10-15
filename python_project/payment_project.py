import qrcode
import PIL
# Taking UPI ID as a input

while True:
    upi_id = input("Enter your upi id = ")

# Basic UPI ID FORMAT VALIDATION
    if (
        upi_id.count("@") == 1
        and " " not in upi_id
        and all(upi_id.split("@"))
    ):
        print("UPI ID format looks Valid!")
        break
    else:
        print("Wrong UPI ID! Please try again.\n")
    
# payement url format
# upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=Message

# Defining the payement URL based on the UPI ID and the payement app
# you can modify these URLs based on the payement apps you want to support

phone_pe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"      #mc is merchant code it is optional
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"    #%20 means just a space or gap btw Recipient (gap) Name
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"


# Create QR Codes for each payement app  
phone_pe_qr = qrcode.make(phone_pe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)


# Save the QR to image file (optional)
# phone_pe_qr.save("phone_pe_qr.png")
# google_pay_qr.save("google_pay_qr.png")
# paytm_qr.save("paytm_qr.png")


# Display the QR Codes (you may need to install PIL//Pillow Library)

phone_pe_qr.show()
google_pay_qr.show()
paytm_qr.show()
