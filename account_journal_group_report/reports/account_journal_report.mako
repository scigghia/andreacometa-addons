<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body class="font_10" style="margin:0px;padding:0px;">

<br/>
<center><H1>${_("ACCOUNT JOURNAL REPORT by GROUP")}</H1></center>

    <table class="font_9 w100 bordi_arrotondati">
        <tr>
			<td style="width:8%; float:left;">${_("DUE DATE")}</td>
			<td style="width:8%; float:left;">${_("DOCUMENT DATE")}</td>
			<td style="width:9%; float:left;">${_("DOCUMENT NR")}</td>
			<td class="w25"><p class="centered">${_("PARTNER")}</p></td>
			<td class="w10"><p class="centered">${_("PAYMENT")}</p></td>
			<td class="w10"><p class="centered">${_("CREDIT")}</p></td>
			<td class="w10"><p class="centered">${_("DEBIT")}</p></td>
			<td class="w20"><p class="centered">${_("ACCOUNT")}</p></td>
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
				<td class="w10"><p style="text-align:left;">${line.name or ''}</p></td>
				<td class="w25"><p style="text-align:left;">${line.partner_id.name or ''}</p></td>
				<td class="w10"><p style="text-align:left;">${line.date or ''}</p></td>
				<td class="w10"><p style="text-align:left;">${line.ref or ''}</p></td>
				<td class="w15"><p style="text-align:left;">''</p></td>
				<td class="w10"><p style="text-align:right;">${formatLang(line.amount or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="w10"><p style="text-align:right;">&nbsp;</p></td>
				<td class="w10"><p style="text-align:right;">&nbsp;</p></td>
			</tr>
			<%tot_importo += line.amount %>
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
			<td class="w10"><p style="text-align:right; font-weight: bold;">&nbsp;</p></td>
			<td class="w10"><p style="text-align:right; font-weight: bold;">&nbsp;</p></td>
		</tr>
    </table>
    
	<div class="clear">&nbsp;</div>
	

</body>
</html>
