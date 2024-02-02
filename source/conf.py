# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2022, test'
author = 'test'
release = '1.1'

version = "1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# 模板的存放路径， 自定义主题时使用
templates_path = ['_templates']

language = 'zh_CN'

# 构建需要的sphinx版本, 可以控制构建的最低sphinx版本
# 当版本低于设置版本时则无法构建
needs_sphinx = '5.3.0'

# 构建所需的插件,
# 当不存在所设置的插件时，则会触发警告，不会停止构建
# needs_extensions = {'sphinxcontrib.something': '1.5'}

# Options for extensions
import os
import sys

sys.path.append(os.path.abspath("./_ext"))

extensions = ['myst_parser', 'sphinx_rtd_theme']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html的主题，默认为alabaster，自带主题详细可见:https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
html_theme = 'sphinx_rtd_theme'

# html主题的相关设置
html_theme_options = {"collapse_navigation": False, "navigation_depth": 6}

# sphinx_rtd_theme 的相关配置
# canonical_url =
# analytics_id =
# analytics_anonymize_ip = False
# collapse_navigation = True
# sticky_navigation = True
# navigation_depth = 4
# includehidden = True
# titles_only =
# logo_only =
# display_version = True
# prev_next_buttons_location = bottom
# style_external_links = False
# style_nav_header_background =
# vcs_pageview_mode =

# 静态文件的存放路径，例如css、js等，默认生成完后会输出到_static文件夹
# 由于不需要构建此文件夹的文件，会自动忽略
html_static_path = ['_static']

# 自定义js文件，路径必须是相对于html_static_path的路径， 也可以使用Sphinx.add_css_files()动态添加
html_js_files = []

# 自定义css文件，路径必须是相对于html_static_path的路径，也可以使用Sphinx.add_css_files()动态添加
html_css_files = []

# 与文档无关的其他资源的路径，由于无需构建此文件夹的文件，会自动忽略
# 默认情况下，此路径下的文件会输出到生成的html的根目录
html_extra_path = ["_extra"]

# 在页面底部显示上一次更新于某某时间
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

# 给每个标题或者描述添加永久链接, 默认为True,
# 最好去除放置出现析构函数无法正常跳转问题
html_permalinks = False

# 自定义左侧栏
# html_sidebars = {
#     '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
# }

# 默认生成的html的文件后缀名， 默认为.html
html_file_suffix = ".html"

# 生成的html文件的后缀，一般与html_file_suffix保持一致
html_link_suffix = ".html"

# 是否显示copyright, 默认为True
html_show_copyright = True

# 是否显示页面下方的由sphinx创建, 默认为True
html_show_sphinx = True

# html全局索引的语言
# html_search_language = 'zh'

html_search_options = {'dict': r"source/jieba.txt"}

# 为不同类型的源文件选择不同的解析器
# source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}


# 识别不同的扩展名为源文件，默认情况下只会将rst识别为源文件
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# 根文档的rst文件的文档名称，其实就是source下面的index.rst文件的名称，可以自定义
root_doc = "index"

# 查找源文件时排除的规则, 以conf所在路径为基准
# 此处排除的规则也会影响到html_static_path和html_extra_path内容的获取
exclude_patterns = [r"jieba.txt"]

# 与上述exclude_patterns相反，查找源文件的规则，以conf所在路径为基准
# 默认情况下，不设置include_patterns和exclude_patterns，会直接查找conf路径下的所有文件
# 如果include_patterns设置为空列表，会导致所有源文件都无法读取
# include_patterns = []

# 在build时是否将warning警告相关信息显示在输出中， 默认为false
keep_warnings = True

# 抑制警告的方法, 是一个列表
suppress_warnings = []

# 对于无法查找的引用触发警告, 默认为False， 但已触发
# nitpicky = True

# 图形、表格、代码块如果有标题，自动添加编号, 默认为False
numfig = True

# 默认的源代码高亮的语言，默认值为default， 类似于python3
highlight_language = 'default'

# 设置不同类型源代码 高亮的设置，使用的是 Pygments配置，
# 不同语言是不同的配置：https://pygments.org/docs/lexers/
# highlight_options = {}

# 代码高亮的风格, 如未设置，则使用默认样式或者使用sphinx指定的html样式
pygments_style = 'sphinx'

html_title = ""

# locale_dirs = ['./locale/zh_CN/LC_MESSAGES/sphinx.mo']

# 搜索结果是否显示详细细节
html_show_search_summary = True

# 是否显示版本，对于read the doc来说就是左上角的版本号
display_version = True

# 是否显示查看源码链接
html_show_sourcelink = False
