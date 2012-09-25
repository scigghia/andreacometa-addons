<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body class="font_10" style="margin:0px;padding:0px;">

    <table class="font_9 w100 bordi_arrotondati">
        <tr>
			<!--td class="w10">CODICE</td-->
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
		

	<!-- HEADER DOCUMENTO -->
	<!--div class="w100">
		<div class="w40">
			LOGO 
		</div>
		<div class="w5">&nbsp;</div>
		<div class="w45 font_12">
			<span class="font_10"><b>${line.company_id.partner_id.name}</b>
			P.Iva: ${line.company_id.partner_id.vat or '-'} - C.F.: ${line.company_id.partner_id.fiscalcode or '-'}
			<br/>${line.company_id.partner_id.address[0].street or '-'}
			${line.company_id.partner_id.address[0].zip or '-'} - ${line.company_id.partner_id.address[0].city or '-'} (${line.company_id.partner_id.address[0].province.code or '-'})
			<br/>Tel: ${line.company_id.partner_id.address[0].phone or '-'} - Fax: ${line.company_id.partner_id.address[0].fax or '-'}
			</span>
		</div>
		<div class="w10">
			&nbsp;
		</div>
	</div-->
	<div class="clear"></div>

	<!-- DATI AZIENDA E CLIENTE-->
	<!--div class="w100">

		<div class="w50" >
			<div class="w100 bordi_arrotondati">
				<div class="w5">&nbsp;</div>
				<div class="w90 distance">
					<i>Spett.le</i>
					<br/><b>${inv.partner_id.name or ''}</b>
					<br/>${inv.address_invoice_id.street or ''}
					<br/>${inv.address_invoice_id.zip or ''} - ${inv.address_invoice_id.city or ''} (${inv.address_invoice_id.province.code or ''})
					<br/>
					<br/><i>Destinazione</i>
					<br/><b>${inv.address_contact_id.name or ''}</b>
					<br/>${inv.address_contact_id.street or ''}
					<br/>${inv.address_contact_id.zip or ''} - ${inv.address_contact_id.city or ''} (${inv.address_contact_id.province.code or ''})
				</div>
				<div class="w5">&nbsp;</div>
			</div>
		</div>
	</div-->
	<div class="clear">&nbsp;</div>
	

    <table id="content" class="font_9 w100">
		%for line in objects:    
			<tr>
				<!--td class="w10">${line.product_id.code or ''}</td-->
				<td class="w50">${line.name or ''}</td>
				<td class="w5"><p class="centered">${line.uos_id.name or ''}</p></td>
				<td class="amount w5"><p class="centered">${line.quantity or ''}</p></td>
				<td class="amount w10"><p class="centered">${formatLang(line.price_unit or 0.00)}</p></td>
				<td class="amount w10"><p class="centered">${formatLang(line.discount or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="amount w10"><p class="centered">${formatLang(line.price_subtotal or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="amount w10"><p class="centered">${line.invoice_line_tax_id and line.invoice_line_tax_id[0].description or ''}</p></td>
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
