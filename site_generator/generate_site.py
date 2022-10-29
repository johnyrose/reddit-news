import jinja2
from models.website.website import Website


def generate_site(website: Website):
    env = jinja2.Environment()
    template_file_content = open('site_generator/template.html').read()
    template = env.from_string(template_file_content)
    output = template.render(main_article=website.main_article,
                             sub_articles=website.sub_articles,
                             mini_articles=website.mini_articles,
                             news_rows=website.news_rows)
    open('site_generator/output.html', 'w').write(output)
