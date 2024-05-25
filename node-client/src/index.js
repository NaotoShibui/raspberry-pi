"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var raspi_1 = require("raspi");
var raspi_gpio_1 = require("raspi-gpio");
// サーバーのIPアドレスとポート番号
var SERVER_HOST = process.env.SERVER_HOST; // ここをサーバーのIPアドレスに置き換える
var SERVER_PORT = Number(process.env.SERVER_PORT) || 3000;
console.log(SERVER_HOST);
console.log(SERVER_PORT);
(0, raspi_1.init)(function () {
    var input = new raspi_gpio_1.DigitalInput({
        pin: 'GPIO4',
        pullResistor: raspi_gpio_1.PULL_UP
    });
    console.log('init');
    input.on('change', function (value) {
        console.log(value);
    });
});
