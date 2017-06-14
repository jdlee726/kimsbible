 $(function () {
     $(document.body).on('click', '#syntax_enact', function () {
         $(this).html('구절/구문단위가리기');
         $(this).attr('id', 'syntax_disable');
         $('.clauseNode, .phraseNode').each(function () {
             $('.clauseNode').attr('class', 'clause');
             $('.phraseNode').attr('class', 'phrase');
             $('.syntax.clause1.hidden').attr('class', 'syntax clause1');
             $('.syntax.phrase1.hidden').attr('class', 'syntax phrase1');
         });

         $(document.body).on('click', '#syntax_disable', function () {
             $(this).html('구절/구문단위표시');
             $(this).attr('id', 'syntax_enact');
             $('.clause, .phrase').each(function () {
                 $('.clause').attr('class', 'clauseNode');
                 $('.phrase').attr('class', 'phraseNode');
                 $('.syntax.clause1').attr('class', 'syntax clause1 hidden');
                 $('.syntax.phrase1').attr('class', 'syntax phrase1 hidden');
             });
         });
     });
 });
