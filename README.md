# Ulauncher Linkwarden Bookmarks Search

___This extension is currently in WIP. Currently, this extension lists only recent 10 bookmarks from Linkwarden___

This Ulauncher extension allows you to conveniently search your bookmarks stored in Linkwarden directly from your desktop.

## Requirements

Before using this extension, make sure you have the following:

- **Ulauncher:** This extension is built for [Ulauncher](https://ulauncher.io), a fast application launcher for Linux. If you haven't installed Ulauncher yet, you can download it from [here](https://ulauncher.io).
  
- **Python Requests Library:** This extension utilizes the Python Requests library to interact with the Linkwarden API. If you haven't installed the Requests library, you can do so via pip:

```
pip install requests
```

## Installation

1. Clone or download this repository to your local machine.

2. Open Ulauncher preferences by clicking on the Ulauncher icon in the system tray and selecting "Preferences".

3. Go to the "Extensions" tab.

4. Click on the "Add extension" button.

5. Browse to the directory where you cloned or downloaded the `ulauncher-linkwarden` repository and select it.

6. The Linkwarden Bookmarks Search extension should now appear in your Ulauncher extensions list. You can configure its settings from there.

## Configuration

Before using the extension, you need to configure your Linkwarden API credentials. Unfortunately, the Linkwarden API documentation is limited, so you may need to refer to their official documentation or contact support for API endpoint details and authentication methods.

Once you have obtained your API credentials, follow these steps to configure the extension:

1. Click on the Ulauncher icon in the system tray and select "Preferences".

2. Go to the "Extensions" tab.

3. Find "Linkwarden Bookmarks Search" in the extensions list and click on the settings icon.

4. Enter your Linkwarden API credentials in the provided fields.

5. Click "Save" to apply the changes.

## Usage

After configuring the extension, you can use it to search your Linkwarden bookmarks directly from Ulauncher. Simply invoke Ulauncher (by default, using the keyboard shortcut `Ctrl + Space`), use the "lw" keyword <space> your query, to fetch results from linkwarden API. This will display a list of bookmarks matching your search query, allowing you to quickly access the desired link.


## Known issues

* Linkwarden doesn't support `limit` to limit the results
* This extension only list recent 10 bookmarks
* `lw <search>` doesn't show different results though API request show the query.

## Demo

<img aligh="center" src="demo.gif">


Feel free to send pull requests or report issues or reach out to the Linkwarden support team if you encounter any issues or have any questions regarding the usage or configuration of this extension.
