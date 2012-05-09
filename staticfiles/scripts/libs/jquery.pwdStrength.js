/* 
 * Plugin:  Password Strength Tester (jQuery)
 * Author:  Ashit Vora (ashit AT innib DOT com)
 *          http://www.innib.com
 * Modify:	Xuwh
 * Mod date:12/12/2011
 * Date:    04/18/2009
 * 
 * Useage:  After including jQuery,
 *          $('passwordfield').passwordStrength();
 */

$.fn.passwordStrength = function(options) {
    var element = this;
	var __lastStat__ = '';
    /*Apply CSS*/
    var css = {
		//
    };

    /*For future use*/
    //var randomID = "1dakjsd3od9123dhwjxnaisudh932dh9ubqhcxbqhjwbd9321udbhbsajhbad8g3";

    /*Add a Span tag to display the strength of the password*/
    //$(this).after("<span id='" + randomID + "'> </span>");

    /*Observe Key Up event display password Strength Result*/
    $(this).live('keyup', function() {
        var pass = $.trim($(this).val());

        var numericTest = /[0-9]/;
        var lowerCaseAlphaTest = /[a-z]/;
        var upperCaseAlphaTest = /[A-Z]/;
        var symbolsTest = /[.,!@#$%^&*()}{:<>|]/;
        var score = 0;
        var result;

        /*Test for the validations*/
        if (numericTest.test(pass)) {
            score++;
        }
        if (lowerCaseAlphaTest.test(pass)) {
            score + 2;
        }
        if (upperCaseAlphaTest.test(pass)) {
            score + 3;
        }
        if (symbolsTest.test(pass)) {
            score + 5;
        }
        /*Test Complete*/

        /*Calculate the result*/
        if (pass.length == 0) {
            result = "";
        }
        else if (score * pass.length < 6) {
            result = "weak";
        }
        else if (score * pass.length < 12) {
            result = "norm";
        }
        else {
            result = "stro";
        }
        /*Calculate result end*/
        //display result
		if(__lastStat__.length > 0){
			$('#' + __lastStat__).removeClass('on');
		}
        $('#stat-' + result).addClass('on');
		__lastStat__ = 'stat-' + result;
    });

    /*Observe KeyDown event to clear the result*/
    $(this).live('keydown', function() {
        //
    });


    /*Clear the result when the focus is blured*/
    $(this).live('blur', function() {
        //
    });

    return this;
};