import project as p


def test_paint():
    assert p.paint("Hello World", "green", "italic") == "\033[3;32mHello World\033[0;0m"


def test_find_urls():
    assert p.find_urls("<a href='link'>") == {("href='link'", "href", "link")}
    assert p.find_urls("<a href='link?something#part'>") == {
        ("href='link?something#part'", "href", "link")
    }


def test_address():
    assert p.address("https://a.com/index.html") == (
        "a_com/index.html",
        "a_com/",
        "index.html",
    )
    assert p.address("https://a.com/b/c/styles.css") == (
        "a_com/b/c/styles.css",
        "a_com/b/c/",
        "styles.css",
    )
    assert p.address("https://a.com") == ("a_com/index.html", "a_com/", "index.html")
    assert p.address("https://a.com/b/c") == (
        "a_com/b/c/index.html",
        "a_com/b/c/",
        "index.html",
    )
