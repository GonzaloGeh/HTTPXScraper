from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start tag: {tag}")
        for attr in attrs:
            print(f"     attr: {attr}")

    def handle_endtag(self, tag):
        print(f"End tag: {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Start-end tag: {tag}")

    def handle_data(self, data):
        print(f"Data: {data}")

    def handle_entityref(self, name):
        print(f"Named entity: {name}")

    def handle_charref(self, name):
        print(f"Numeric entity: {name}")