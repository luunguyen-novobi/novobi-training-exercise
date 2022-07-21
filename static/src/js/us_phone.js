odoo.define('purchase_order_enhancement.us_phone', function (require) {
'use strict';

function normalize(phone) {
    //normalize string and remove all unnecessary characters
    phone = phone.replace(/[^\d]/g, "");

    //check if number length equals to 10
    if (phone.length == 10) {
        //reformat and return phone number
        return phone.replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3");
    }

    return phone;
}

var FieldChar = require('web.basic_fields').FieldChar;

var UsPhoneFormat = FieldChar.extend({
    events: _.extend({}, FieldChar.prototype.events, {
        'keyup': '_onKeyUp'
    }),

    _onKeyUp: function(e) {
        e.preventDefault();
        e.target.value = normalize(e.target.value);
    }
});

var field_registry = require('web.field_registry');
field_registry.add('usphone_format', UsPhoneFormat);

return UsPhoneFormat;

});
