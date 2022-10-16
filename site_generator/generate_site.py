import jinja2


# JINJA TEMPLATE:

# Main: main_article_title, main_article_text, main_article_image
# Sub articles =


def generate_site():
    env = jinja2.Environment()
    template_file_content = open('site_generator/template.html').read()
    template = env.from_string(template_file_content)

    main_article = {
        'title': 'Main article title',
        'text': 'Main article text',
        'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
        "author": "John Smith",
        "url": "https://www.google.com",
    }
    sub_articles = [
        {
            'title': 'Sub article title',
            'text': 'Sub article text',
            'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
            "author": "John Smith",
            "url": "https://www.google.com",
        },
        {
            'title': 'Sub article title',
            'text': 'Sub article text',
            'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
            "author": "John Smith",
            "url": "https://www.google.com",
        },
    ]
    mini_articles = [
        {
            'title': 'Sub article title',
            'text': 'Sub article text',
            'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
            "author": "John Smith",
            "url": "https://www.google.com",
        },
        {
            'title': 'Sub article title',
            'text': 'Sub article text',
            'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
            "author": "John Smith",
            "url": "https://www.google.com",
        },
        {
            'title': 'Sub article title',
            'text': 'Sub article text',
            'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
            "author": "John Smith",
            "url": "https://www.google.com",
        },
    ]
    news_rows = [  # Only supports 3 articles or less
        {
            "name": "r/worldnews",
            "articles": [
                {
                    'title': 'Sub article title',
                    'text': 'Sub article text',
                    'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
                    "author": "John Smith",
                    "url": "https://www.google.com",
                },
                {
                    'title': 'Sub article title',
                    'text': 'Sub article text',
                    'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
                    "author": "John Smith",
                    "url": "https://www.google.com",
                },
                {
                    'title': 'Sub article title',
                    'text': 'Sub article text',
                    'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
                    "author": "John Smith",
                    "url": "https://www.google.com",
                },
            ]
        },
        {
            "name": "r/programming",
            "articles": [
                {
                    'title': 'Sub article title',
                    'text': 'Sub article text',
                    'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
                    "author": "John Smith",
                    "url": "https://www.google.com",
                },
                {
                    'title': 'Sub article title',
                    'text': 'Sub article text',
                    'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
                    "author": "John Smith",
                    "url": "https://www.google.com",
                },
                {
                    'title': 'Sub article title',
                    'text': 'Sub article text',
                    'image': 'https://4.img-dpreview.com/files/p/articles/5081755051/0652566517.jpeg',
                    "author": "John Smith",
                    "url": "https://www.google.com",
                },
            ]
        }
    ]

    output = template.render(main_article=main_article, sub_articles=sub_articles, mini_articles=mini_articles,
                             news_rows=news_rows)
    open('site_generator/output.html', 'w').write(output)
