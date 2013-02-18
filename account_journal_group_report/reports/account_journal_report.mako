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
			<td style="width:6%; float:left;">${_("DATE")}</td>
			<td style="width:10%; float:left;">${_("DOCUMENT")}</td>
			<td style="width:6%; float:left;">${_("DOCUMENT DATE")}</td>
			<td style="width:8%; float:left;">${_("REF")}</td>
			<td class="w30"><p style="text-align:left;">${_("PARTNER")}</p></td>
			<td class="w20"><p style="text-align:left;">${_("PAYMENT TERMS")}</p></td>
			<td class="w10"><p style="text-align:left;">${_("CREDIT")}</p></td>
			<td class="w10"><p style="text-align:left;">${_("DEBIT")}</p></td>
		</tr>
	</table>
		

	<div class="clear"></div>

    <table id="content" class="font_9 w100">
		<% tot_amount = 0 %>
		<% big_credit = 0 %>
		<% big_debit = 0 %>
		%for move in objects:
		%if move:    
			<tr>
				<% tot_credit = 0 %>
				<% tot_debit = 0 %>
				<% line_name = '' %>
				<% line_name_tmp = '' %>
				<% date_i = '' %>
				<% payment_terms = '' %>
				% if move.line_id:
				%for line in move.line_id:
					%if line.account_id.type in ('payable', 'receivable'):
						<% tot_debit += line.debit%>
						<% tot_credit +=  line.credit%>
						%if line.reconcile_id.line_id != None:
							<% line_rec_ids = line.reconcile_id.line_id %>
						%elif line.reconcile_partial_id.line_partial_ids != None:
							<% line_rec_ids = line.reconcile_partial_id.line_partial_ids %>
						%else:
							<% line_rec_ids = None %>
						%endif
						%if line_rec_ids != None:
							% for ll in line_rec_ids:
								%if ll.invoice != None:
									%if ll.invoice.type == 'out_invoice':
										<% line_name_tmp = ll.invoice.number or ''%>
									%else:
										<% line_name_tmp = ll.invoice.origin or ''%>
									%endif
									%if line_name == '' or line_name == None:
										<% line_name = line_name_tmp %>
									%else:
										<% line_name = '%s, %s' % (line_name, line_name_tmp) %>
									%endif
									%if ll.invoice.date_invoice != None:
										%if date_i == '':
											<% date_i = ll.invoice.date_invoice %>
										%else:
											<% date_i = '%s, %s' % (date_i, ll.invoice.date_invoice) %>
										%endif
										%if payment_terms == '' and ll.invoice.payment_term != None:
											<% payment_terms = ll.invoice.payment_term.name %>
										%endif
									%endif
								%endif
							%endfor
						%endif
					%endif
				%endfor
				%endif
				<td style="width:6%; float:left;">${move.date or ''}</td>
				<td style="width:10%; float:left;">${line_name or ''}</td>
				<td style="width:6%; float:left;">${date_i}</td>
				<td style="width:8%; float:left;">${move.ref or ''}</td>
				<td class="w30"><p style="text-align:left;">${move.line_id and move.line_id[0].partner_id.name or ''}</p></td>
				<td class="w20"><p style="text-align:left;">${payment_terms}</p></td>
				<td class="w10"><p style="text-align:right;">${formatLang(tot_credit or 0.00, digits=get_digits(dp='Account'))}</p></td>
				<td class="w10"><p style="text-align:right;">${formatLang(tot_debit or 0.00, digits=get_digits(dp='Account'))}</p></td>
			</tr>
			<%tot_amount += tot_credit - tot_debit %>
			<%big_credit += tot_credit %>
			<%big_debit += tot_debit %>
		%endif
        %endfor
        <tr><td colspan=8><hr style="width:100%"></td></tr>
		<tr style="height:100%">
			<td class="font_10" colspan="2"><b>${_("CREDIT:")} ${formatLang(big_credit or 0.00, digits=get_digits(dp='Account'))}</b></td>
			<td class="font_10" colspan="2"><b>${_("DEBIT:")} ${formatLang(big_debit or 0.00, digits=get_digits(dp='Account'))}</b></td>
			<td class="font_10" colspan="4"><b>${_("TOTAL:")} ${formatLang(tot_amount or 0.00, digits=get_digits(dp='Account'))}</b></td>
		</tr>
    </table>
    
	<div class="clear">&nbsp;</div>
	

</body>
</html>
