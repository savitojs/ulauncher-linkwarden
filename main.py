import logging
import requests
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.client.EventListener import EventListener

logger = logging.getLogger(__name__)

class LinkwardenExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_argument() or ""

        api_url = extension.preferences['api_url']
        api_token = extension.preferences['api_token']

        headers = {
                "Authorization": f"Bearer {api_token}",
                "Cache-Control": "no-cache"
        }

        params = {
            "sort": 0,
            "searchQueryString": query,
            "searchByName": True,
            "searchByUrl": True,
            "searchByDescription": True,
            "searchByTags": True,
            "searchByTextContent": False
        }

        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            logger.debug("Incoming API response: %s", data)

            items = []
            for item in data["response"]:
                items.append(
                    ExtensionResultItem(
                        icon='images/icon.png',
                        name=item["name"],
                        description=item["url"],
                        on_enter=CopyToClipboardAction(item["url"])
                    )
                )

            items = items[:10]

            return RenderResultListAction(items)

        except requests.exceptions.RequestException as e:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="HTTP Error",
                    description="An HTTP error occurred: {}".format(e)
                )
            ])

        except Exception as e:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="Error",
                    description="An error occurred: {}".format(e)
                )
            ])

if __name__ == '__main__':
    LinkwardenExtension().run()
