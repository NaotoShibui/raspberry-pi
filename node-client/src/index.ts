const { init, DigitalInput } = require('raspi');
const { ON, LOW } = require('raspi-gpio');
const net = require('net');

// サーバーのIPアドレスとポート番号
const SERVER_HOST = process.env.SERVER_HOST; // ここをサーバーのIPアドレスに置き換える
const SERVER_PORT = Number(process.env.SERVER_PORT) || 3000;

const client = net.createConnection({ host: SERVER_HOST, port: SERVER_PORT }, () => console.log('Connected.'));

init(() => {
  const button = new DigitalInput({
    pin: 'GPIO4',
    pullResistor: ON
  });

  setInterval(() => {
    if (button.read() === LOW) {
      console.log('Turn on.');
      client.write('Turn on.');
    }
  }, Number(process.env.INTERVAL) || 100);
});

// 接続が切断された場合
client.on('end', () => {
  console.log('サーバーから切断されました。');
});

// プログラム終了時にGPIOのリソースを解放
process.on('SIGINT', () => {
  client.end();
  process.exit();
});
