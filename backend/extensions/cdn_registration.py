# services/app_cdns.py
from flask_bootstrap import WebCDN


def register_app_cdn(app):
    # DataTable for displaying information in a grid
    app.extensions['bootstrap']['cdns']['dataTable'] = WebCDN(
        'https://cdn.datatables.net/1.10.19/'
    )
    # Buttons for saving/printing
    app.extensions['bootstrap']['cdns']['dataTableBtns'] = WebCDN(
        'https://cdn.datatables.net/buttons/1.5.1/'
    )
    app.extensions['bootstrap']['cdns']['saveJs'] = WebCDN(
        'https://cdnjs.cloudflare.com/ajax/libs/'
    )
    app.extensions['bootstrap']['cdns']['multiselect'] = WebCDN(
        'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/'
    )
    app.extensions['bootstrap']['cdns']['fontAwesome'] = WebCDN(
        'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/'
    )
