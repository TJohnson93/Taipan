title: Share your WiFi Password with a QR Code - Part 2
date: 2016-10-22
date_long: 22 October 2016
author: Todd Johnson
banner: code_bg.jpg

So in [Part 1](http://blog.toddjohnson.com.au/share-your-wifi-password-with-a-qr-code-part-1/), we went through the steps to create a QR code for family and friends to scan to automatically connect them to your network. As you might have discovered, this method worked amazing for those with Android devices, and not so great for iOS devices. After scanning the QR Code on iOS you would've seen this:

![Output of QR Scan on iOS](/content/images/2016/10/qr-code-ios-2.png)

Which is ok, the user will just need to copy and paste SSID and password into the Settings app.

![iOS copy & paste network details - GIF]

This didn't really sit to well with me so I set out to find an alternative! I discovered that by using a tool common in organisations that manage Apple device, it's possible to create a profile which can then be downloaded and installed onto any iOS device. So how does this help? You can create a configuration profile that contains your networks credentials so that when an iOS device downloads this profile it can connect straight away.
**Note:** This method requires a Mac computer to create the configuration profile.

![Apple Configurator 2](/content/images/2016/10/app-logo-apple-configurator.jpg)


Keeping in sync with the QR Code theme, how can we download this profile? I decided that the best way to distribute this profile is to save it on to Dropbox and embed the Dropbox link into the QR Code. This means that when an iOS device scans the QR Code it will open the Dropbox link so the user can download and install the configuration profile. It's not as streamlined as on an Android device, but, pressing a couple of buttons is easier than typing a long, complex password or copy, switching apps and pasting the password manually.

So let's get started! Below we will discuss the following steps.

* Creating a configuration profile for iOS devices
* Creating a Dropbox account and Uploading your new configuration profile
* Creating a QR Code that links to your configuration profile stored on Dropbox

## Create Configuration Profile

So what is an configuration profile? It's similar to Windows Group Policies or Windows Registry, essentially it can provide rules for a device that its installed on.

To create a configuration profile, you'll need a Mac computer and download the [Apple Configurator](https://geo.itunes.apple.com/us/app/apple-configurator-2/id1037126344?mt=12&at=1010loXs&ct=253325) app from the Mac App Store.

Once installed launch **Apple Configurator** and click **File > New Profile**.

![Create a New Profile](/content/images/2016/10/config-profile-create-new.png)

Once the new profile page loads, ensure that the General tab is selected. Type a name for your profile into the Name field. **Note:** Make your name descriptive as this is what will be shown on the iOS devices once downloaded and installed.

The rest of the fields are optional and more suited towards organisations looking to further lock down their devices. We will however use the Automatically Remove Profile option. This will ensure that your guests are only using your WiFi whilst they are there. Change **Never** to whichever timeframe you'd like (I am going to set it to expire after 24 hours) or you can have to not expire, whichever suits you.

![General Tab](/content/images/2016/10/config-profile-general-tab.gif)

**Click** on the **Wifi** tab on the left hand side. This is where we set up the functionality of our profile.

Enter the following details:

* SSID (Your network name)
* Check the Auto Join checkbox
* Choose your Network Type from the drop down options.

![WiFi tab](/content/images/2016/10/config-profile-wifi-tab.gif)

Once your done, click on **File > Save** to save your configuration profile to your Mac.

![Saving Configuration Profile](/content/images/2016/10/config-profile-save.png)

In the next section we are going to create a Dropbox account and upload our configuration profile that we just created.


## Create Dropbox Account and Uploading Configuration Profile

Now that we have our configuration profile, we need somewhere it can live, ready to be installed.

Enter Dropbox! Chances are that you have heard about Dropbox, the free cloud sharing service, if not head on over and [create an account](https://www.dropbox.com/).

Once you have your Dropbox account, log in and navigate to your public folder and upload your configuration profile.

![Upload configuration profile](/content/images/2016/10/dropbox-upload.gif)

Once your configuration profile has finished uploading, click on the Share button and copy the link provided to your clipboard. We will need this for the next step!

![Copy Share Link](/content/images/2016/10/dropbox-share-link.gif)

## Create new QR Code to Download Configuration Profile

So lets go back to [UniTag](https://www.unitag.io/qrcode) and click on the **Start and create a QR Code** button.

![Create a QR Code](/content/images/2016/10/01.png)

On the next page, select Static again, but this time paste your dropbox link (the one we copied earlier) into the Destination URL field and click on the Confirm button.

![Generate QR Code](/content/images/2016/10/unitag-generate.gif)

Easy, don't forget to click on the **Save and Close** button to the right of your QR Code.

Now when your family and friends scan your QR Code, all they need to do is click **Install** and they now have access to your network. No password sharing needed!

![iOS Profile Install - Complete Process](/content/images/2016/10/ios-full-process.gif)

Let me know in the comments if you'd like more information or any other questions about anything tech and I'll do my best to answer them!
