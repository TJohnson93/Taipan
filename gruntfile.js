// Gruntfile.js
module.exports = function (grunt) {

  // measures the time each task takes
  require('time-grunt')(grunt);

  // load tasks
  require('load-grunt-tasks')(grunt);

  // define grunt options
  var options = {
    config : {
      src : "config/grunt/*.js"
    }
  };

  // loads the various task configuration files
  var configs = require('load-grunt-configs')(grunt, options);
  grunt.initConfig(configs);

  // Register tasks
  grunt.registerTask('default', [
    'less:development'
  ]);

  grunt.registerTask('dev', [
    'newer:less:production',
  ]);

  grunt.registerTask('prod', [
    'dev', // Run Development Build
    'newer:less:production',
  ]);

  grunt.registerTask('serve', [

  ]);
}
