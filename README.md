# Reddit News Site

This is a small Python project that generates a minimalistic news site from Reddit posts. 

A [Static hosted demo](https://johnyrose.github.io/reddit-news-static-demo/) can be found here.

## Background

The project uses 3 external APIs to achieve the generated news site:
 * [Reddit API](https://www.reddit.com/dev/api/) (Using the Praw library) to get posts from Reddit
 * [URLMeta](https://home.urlmeta.org/) To extract display images from the links in the posts
 * [ExtractorAPI](https://extractorapi.com/) To extract the article text from the links in the posts

The used website template is based on [News-journal](https://beefree.io/template/news-journal/) by [Andrea Dall'Ara](https://beefree.io/designer/andrea-dallara/).

The site generation flow generally goes through the following stages:
 * **Data collection**:
   * Get news posts from Reddit (from the configured subreddits)
   * Generate a usable article from each post by extracting the article text and image from the post's link
 * **Site generation**:
   * Go through the generated articles and choose which articles will appear on the site
   * Generate a static site from the chosen articles with a Jinja template.

## Quickstart

This section will guide you through the quickest way to get the site up and running. A more detailed explanation of the project's configuration can be found in the [Configuration](#configuration) section.

### Prerequisites:

Before you run the project, you'll need to generate API keys for the following services:
 * [Reddit API](https://www.reddit.com/prefs/apps/)
 * [URLMeta](https://home.urlmeta.org/)
 * [ExtractorAPI](https://extractorapi.com/)

Each of these services has a free tier that should be enough for this project, none of them require any payment information, and getting the keys for all 3 should take no longer than 10 minutes.

From each API, make sure you have the following data:
 * Reddit API:
   * Username
   * Password
   * Client ID
   * Client Secret
 * URLMeta:
   * API Key
 * ExtractorAPI:
   * API Key

Also, **Python 3.8+** needs to be installed on your machine.

### Setup

* Clone this repository and enter the project's directory
    ```commandline
    git clone https://github.com/johnyrose/reddit-news
    cd reddit-news
    ```
* Install the project's dependencies
    ```commandline
    pip install -r requirements.txt
    ```
* Create a file named `config.json` in the project's root directory. This file will contain the configuration for the project. Copy the following content to the file:
    ```json
    {
        "tasks_to_perform": {
            "data_collection": true,
            "website_generation": true
        },
        "external_apis": {
            "reddit": {
                "user": "<Your Reddit username>",
                "password": "<Your Reddit password>",
                "clientId": "<Your Reddit Client ID>",
                "clientSecret": "<Your Reddit Client Secret>",
                "userAgent": "bla"
            },
            "extractor": {
                "url": "https://extractorapi.com/api/v1/extractor",
                "api_token": "<Your ExtractorAPI API Key>"
            },
            "urlmeta": {
                "url": "https://api.urlmeta.org",
                "email": "<Your Email>",
                "api_token": "<Your URLMeta API Key>"
            }
        },
        "general_settings": {
            "db_file": "sqlite.db",
            "enable_sqlalchemy_logging": false,
            "template_file": "site_generator/template.jinja2",
            "output_file": "output.html",
            "local_images_folder": "images",
            "use_local_images": true,
            "max_parallel_requests": 1
        },
        "subreddits": [
            {
                "name": "worldnews",
                "posts": 15,
                "ignoreStickied": true
            },
            {
                "name": "technews",
                "posts": 10,
                "ignoreStickied": true
            },
            {
                "name": "UpliftingNews",
                "posts": 6,
                "ignoreStickied": true
            }
        ],
        "website": {
            "text_length": {
                "main_article": 500,
                "sub_articles": 200,
                "mini_articles": 100,
                "news_rows_articles": 150,
                "titles": 170
            },
            "articles_amount": {
                "sub_articles": 4,
                "mini_articles": 5,
                "news_row_articles": 3
            },
            "sorting_method": "score"
        }
    }
    ```
  * Replace the values in the `external_apis` section with the API keys you generated earlier
  * Run the project
    ```commandline
    python main.py
    ```
  * The generated site will be saved in the `output.html` file in the project's root directory. Double click the file to open it in your browser.
  * You should now see the generated site in your browser. 

## Configuration

This section will elaborate on the options available in the project's configuration file. The config template can be found in the [Quickstart](#quickstart) section.

### tasks_to_perform: 

This section contains a boolean value for each of the project's tasks. Setting a task's value to `true` will cause the task to be performed when the project is run. Setting a task's value to `false` will cause the task to be skipped when the project is run.

This can be useful when you already ran the data collection phase and want to play around with the config when generating the site.
 * **data_collection**: Whether to perform the data collection task. If set to `false`, the project will skip the data collection task and use the existing data from the database instead.
 * **website_generation**: Whether to perform the website generation task.

### subreddits:

This section contains a list of subreddits to get posts from. Each subreddit is represented by a dictionary with the following fields:
 * **name**: The name of the subreddit to get posts from. This is the name that appears in the subreddit's URL. For example, the name of the [r/worldnews](https://www.reddit.com/r/worldnews/) subreddit is `worldnews`.
 * **posts**: The amount of posts to get from the subreddit. 
 * **ignoreStickied**: Whether to ignore stickied posts.

I highly suggest trying different subreddits and seeing different results.

### general_settings:

These are general settings for the project. For the most part, I'd suggest leaving them as they are in the example above.

  * **db_file**: The path to the SQLITE database file.
  * **enable_sqlalchemy_logging**: Whether to enable SQLAlchemy logging.
  * **template_file**: The path to the template file to use when generating the site.
  * **output_file**: The path to the output file to save the generated site to.
  * **use_local_images**: Whether to download the images locally when generating the site. Setting this to `false` will use the original image URLs instead. This can cause some of the images to be broken after a while.
  * **local_images_folder**: The path to the folder to save the images to (only relevant if `use_local_images` is set to `true`).
  * **max_parallel_requests**: The maximum amount of parallel requests to make to the external APIs. This can be useful if you want to limit the amount of requests you make to the external APIs.

### website:
* **text_length**: The maximum length of the text to display in the generated site for each type of article.
* **articles_amount**: The amount of articles to display in the generated site for each type of article.
  * **Note**: Setting the `news_row` setting to a value higher than 3 will cause the site to look weird. 
* **sorting_method**: The sorting method to use when sorting the articles in the generated site. Can be either `score` or `relative_upvotes`.
  * **score**: Sorts the articles by their score (upvotes).
  * **relative_upvotes**: Sorts the articles by their relative upvotes. This is calculated by dividing the article's upvotes by the amount of upvotes the article with the most upvotes has.
    * This method is a weird attempt to balance the article order between the different subreddit. It doesn't always work well, and I'd suggest trying it only if you're unsatisfied with the results of the `score` method.


Thank you for checking out the project and I hope you enjoy using it! Feel free to contact me for any suggestions, feedback of questions.
