function(modal) {
    $('.link-types a', modal.body).click(function() {
        modal.loadUrl(this.href);
        return false;
    });

    {% include 'verdantadmin/chooser/_search_behaviour.js' %}
    ajaxifySearchResults();
}
