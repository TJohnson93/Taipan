module.exports = {
  development: {
    options: {
      paths: ['src/less']
    },
    files: {
      'src/static/css/app.css' : [
        'src/static/less/app.less'
      ]
    }
  },
  production: {
    options: {
      compress: true,
      paths: ['src/css']
    },
    files: {
      'dist/css/app-min.css' : 'src/css/app-min.css'
    }
  }
}
