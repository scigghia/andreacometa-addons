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
			<td class="w10">Sezionale</td>
			<td class="w25"><p class="centered">Partner</p></td>
			<td class="w10"><p class="centered">Scadenza</p></td>
			<td class="w10"><p class="centered">Fattura</p></td>
			<td class="w15"><p class="centered">Pagamento</p></td>
			<td class="w10"><p class="centered">Importo</p></td>
			<td class="w10"><p class="centered">Dare</p></td>
			<td class="w10"><p class="centered">Avere</p></td>
		</tr>
	</table>
		


	<div class="clear"></div>

    <table id="content" class="font_9 w100">
		<% tot_importo = 0 %>
		<% tot_dare = 0 %>
		<% tot_avere = 0 %>
		%for line in objects:
		%if line:    
			<tr>
				<td class="w10"><p style="text-align:left;">${line.invoice.journal_id and line.invoice.journal_id.code or ''}</p></td>
				<td class="w25"><p style="text-align:left;">${line.partner_id.name or ''}</p></td>
				<td class="w10"><p style="text-align:left;">${line.date_maturity or line.date}</p></td>
				<td class="w10"><p style="text-align:left;">${line.invoice.number or line.name or ''}</p></td>
				<td class="w15"><p style="text-align:left;">${line.invoice.payment_term and line.invoice.payment_term.name or ''}</p></td>
				<td class="w10"><p style="text-align:right;">${formatLang(line.amount_residual or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="w10"><p style="text-align:right;">${formatLang(line.debit or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="w10"><p style="text-align:right;">${formatLang(line.credit or 0.00, digits=get_digits(dp='Account'))}</p></td>
			</tr>
			%if line.debit == 0.0:
				<%tot_importo -= line.amount_residual %>
			%else:
				<%tot_importo += line.amount_residual %>
			%endif
			<% tot_dare += line.debit %>
			<% tot_avere += line.credit %>
		%endif
        %endfor
        <tr><td colspan=8><hr style="width:100%"></td></tr>
		<tr style="height:100%">
			<td class="w10">&nbsp;</td>
			<td class="w25">&nbsp;</td>
			<td class="w10">&nbsp;</td>
			<td class="w10">&nbsp;</td>
			<td class="w15">&nbsp;</td>
			<td class="w10"><p style="text-align:right; font-weight: bold;">${tot_importo}</p></td>
			<td class="w10"><p style="text-align:right; font-weight: bold;">${tot_dare}</p></td>
			<td class="w10"><p style="text-align:right; font-weight: bold;">${tot_avere}</p></td>
		</tr>
    </table>
    
	<div class="clear">&nbsp;</div>
	

</body>
</html>
