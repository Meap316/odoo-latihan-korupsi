odoo.define('persenan_plus.tree_view_button', function (require){
    "use strict";

    var ajax = require('web.ajax');
    var ListController = require('web.ListController');

    var rpc = require('web.rpc')

    ListController.include({
        renderButtons: function($node) {
            this._super.apply(this, arguments);
            var self = this;
            if (this.$buttons) {
                $(this.$buttons).find('.oe_new_custom_button').on('click', function() {
                    rpc.query({
                        model: 'persenan_plus.oknum',
                        method: 'boop',
                        args: [],
                    }).then(function(res){
                        // console.log(res)
                        // self.reload();
                    })
                });
            }
        },
    });
});