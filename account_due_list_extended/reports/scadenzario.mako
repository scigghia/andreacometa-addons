<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body class="font_10" style="margin:0px;padding:0px;">

<br/>
<center><H1>SCADENZARIO</H1></center>

    <table class="font_9 w100 bordi_arrotondati">
        <tr>
			<td class="w20">Numero Movimento</td>
			<td class="w5"><p class="centered">Partner</p></td>
			<td class="w5"><p class="centered">Termini</p></td>
			<td class="w10"><p class="centered">Tipo</p></td>
			<td class="w10"><p class="centered">Scadenza</p></td>
			<td class="w10"><p class="centered">Fattura</p></td>
			<td class="w10"><p class="centered">Pagamento</p></td>
			<td class="w10"><p class="centered">Importo</p></td>
			<td class="w10"><p class="centered">Dare</p></td>
			<td class="w10"><p class="centered">Avere</p></td>
		</tr>
	</table>
		


	<div class="clear"></div>

    <table id="content" class="font_9 w100">
		%for line in objects:    
			<tr>
				<td class="w20">${line.name or ''}</td>
				<td class="w5"><p class="centered">${line.move_id.partner_id.name or ''}</p></td>
				<td class="w5"><p class="centered">Termini</p></td>
				<td class="w10"><p class="centered">Tipo</p></td>
				<td class="w10"><p class="centered">${line.date_maturity or line.date}</p></td>
				<td class="w10"><p class="centered">Fattura</p></td>
				<td class="w10"><p class="centered">Pagamento</p></td>
				<td class="w10"><p class="centered">${formatLang(line.amount_residual or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="w10"><p class="centered">${formatLang(line.debit or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="w10"><p class="centered">${formatLang(line.credit or 0.00, digits=get_digits(dp='Account'))}</p></td>
			</tr>
        %endfor
		<tr style="height:100%">
			<td><script>
				var divh = document.getElementById('content').offsetHeight;
				var max_h_1 = 430;
				/*var max_h_n = 550;*/
				var max_h_n = max_h_1 + 10

				var is_one = divh/max_h_1;

				if (is_one<=0) {
					is_one = true;
					document.getElementById('content').style.height=max_h_1;
				}
				else {
					is_one = false;
				}

				if (!is_one) {
					var pages = (Math.ceil((divh-max_h_1)/max_h_n)).toFixed(1);

					document.getElementById('content').style.height=max_h_n*pages+max_h_1;
				}
				</script>
			</td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>
    </table>
    
	<div class="clear">&nbsp;</div>
	

</body>
</html>
