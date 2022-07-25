odoo.define('purchase_order_enhancement.usphone_format', function (require) {
'use strict';

var FieldChar = require('web.basic_fields').FieldChar;

var UsPhoneFormat = FieldChar.extend({
    convertPhoneToUSFormat: function(phone) {
        phone = phone.replace(/[^\d]/g, "");
        if (phone.length == 10) {
            return phone.replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
        }
        return phone;
    },

    events: _.extend({}, FieldChar.prototype.events, {
        'change': '_onChange'
    }),

    _onChange: function(e) {
        var self = this;
        e.preventDefault();
        e.target.value = self.convertPhoneToUSFormat(e.target.value);
    }
});

var field_registry = require('web.field_registry');
field_registry.add('usphone_format', UsPhoneFormat);

return UsPhoneFormat;

});
