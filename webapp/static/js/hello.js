hk = hk || {};

hk.HelloView = BB.View.extend({
    el: '#hello',
    template: _.template($('#hello-template').html()),

    initialize: function (options) {
        this.render();
    },

    render: function () {
        this.$el.empty().append(this.template());
    },

    events: {
    },
});
