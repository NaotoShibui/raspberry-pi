import { init } from 'raspi';
import { DigitalInput, DigitalOutput, PULL_UP, HIGH, LOW } from 'raspi-gpio';
import { request } from 'undici';

// サーバーのIPアドレスとポート番号
const SERVER_HOST = '192.168.0.1';
const SERVER_PORT = Number(process.env.SERVER_PORT) || 3000;

const url = `http://${SERVER_HOST}:${SERVER_PORT}`;
let pin = LOW;

init(() => {
    const input = new DigitalInput({
        pin: 'GPIO4',
        pullResistor: PULL_UP
    });

    console.log('init');

    input.on('change', (value) => {
	if(value === HIGH && value != pin) {
	    console.log(new Date().toISOString());
            fetch(url);
	}
        pin = value;
    });
});


