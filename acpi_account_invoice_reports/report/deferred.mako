<%def name="inv_header(inv,page_number,row_limit,pagina_attuale)">
    <!-- HEADER DOCUMENTO -->
    <div class="w100">
        <div class="w45">
            <center>
                ${helper.embed_logo_by_name('Logo')}
                <b>${inv.company_id.name or ''}</b>
            </center>
            <span class="font_10">${inv.company_id.partner_id.address[0].street or ''}
            <br/>${inv.company_id.partner_id.address[0].zip or ''} - ${inv.company_id.partner_id.address[0].city or ''} (${inv.company_id.partner_id.address[0].province and inv.company_id.partner_id.address[0].province.code or '--'})
            <br/>Tel: ${inv.company_id.partner_id.address[0].phone or ''} - Fax: ${inv.company_id.partner_id.address[0].fax or ''}
            <br/>P.Iva: ${inv.company_id.partner_id.vat or ''} - C.F.: ${inv.company_id.partner_id.fiscalcode or ''}
            </span><span class="font_9">
            %if inv.company_id.bank_ids: 
                <br/><br/><br/><b>${_("Bank Details")}:</b>
                <br/>
            %endif
            %for bank in inv.company_id.bank_ids:
                <p class="font_12">${bank.acc_number or ''} - ${bank.bank_name or ''}</p>
            %endfor
            </span>
        </div>
        <div class="w5">&nbsp;</div>
        <div class="w50" >
            <div class="w100 simple_border">
                <div class="w5">&nbsp;</div>
                <div class="w90 distance">
                    <i>${_("Gentle")}</i>
                    <br/><b>${inv.partner_id.name or ''}</b>
                    <br/>${inv.address_invoice_id.street or ''}
                    <br/>${inv.address_invoice_id.zip or ''} - ${inv.address_invoice_id.city or ''} (${inv.address_invoice_id.province and inv.address_invoice_id.province.code or '--'})
                    <br/>
                    <br/><i>Destinazione</i>
                    <br/><b>${inv.partner_shipping_id.name or ''}</b>
                    <br/>${inv.partner_shipping_id.street or ''}
                    <br/>${inv.partner_shipping_id.zip or ''} - ${inv.partner_shipping_id.city or ''} (${inv.partner_shipping_id.province and inv.partner_shipping_id.province.code or '--'})
                </div>
                <div class="w5">&nbsp;</div>
            </div>
        </div>
    </div>
    <div class="clear">&nbsp;</div>
    
    <div class="w100 simple_border">
        <table class="w100 font_8 info_table">
            <tr>
                <td>
                    <p>${_("DOCUMENT TYPE")}</p>
                    <p class="data">Fattura Immediata</p>
                </td>
                <td>
                    <p>${_("DOCUMENT NUMBER")}</p>
                    <p class="data">${inv.number or 'Bozza'}</p>
                </td>
                <td>
                    <p>${_("DOCUMENT DATE")}</p>
                    <p class="data">&nbsp; ${inv.date_invoice}</p>
                </td>
                <td class="w40">
                    <p>${_("VAT")}</p>
                    <p class="data">${inv.partner_id.vat or '&nbsp;'} </p>
                </td>
                <td>
                    <p>${_("TRANSPORT REASON")}</p>
                    <p class="data">${inv.transportation_reason_id and inv.transportation_reason_id.name or '&nbsp;'}</p>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>${_("PAYMENT")}</p>
                    <p class="data">${inv.payment_term.name or '&nbsp;'}</p>
                </td>
                <td colspan="2">
                    <p>${_("FISCAL CODE")}</p>
                    <p class="data">${inv.partner_id.fiscalcode or '&nbsp;'}</p>
                </td>
                <td>
                    <p>${_("PAG. N.")}</p>
                    <p class="data">${pagina_attuale} / ${page_number(inv.invoice_line, row_limit)}</p>
                </td>
            </tr>
        </table>
    </div>
    <div class="clear">&nbsp;</div>

    <table class="font_9 w100 simple_border">
        <tr>
            <!--td class="w10">CODICE</td-->
            <td class="w50">${_("DESCRIPTION")}</td>
            <td class="w5"><p class="centered">${_("M.U.")}</p></td>
            <td class="w5"><p class="centered">${_("QTY")}</p></td>
            <td class="w10"><p class="centered">${_("PRICE UNIT")}</p></td>
            <td class="w10"><p class="centered">${_("DISCOUNT")}</p></td>
            <td class="w10"><p class="centered">${_("TOTAL")}</p></td>
            <td class="w10"><p class="centered">${_("TAX")}</p></td>
        </tr>
    </table>

    <table id="content" class="font_9 w100">
</%def>

<%def name="inv_footer(inv)">
    </table>
    <div class="clear">&nbsp;</div>
    <!-- Mostra/Nasconde le note ma mantiene le dimensioni dello spazio occupato -->
    <div class="w100 simple_border distance">
        <div class="w5">&nbsp;</div>
        %if inv.comment:
            <div class="w95">${_("NOTES")}:<br />${newlined_text(inv.comment)}</div>
        %else:
            <div class="w95">${_("NOTES")}:<br /><br /></div>
        %endif
        <div class="w5">&nbsp;</div>
    </div>
    <div class="clear">&nbsp;</div>
    
    <div class="w100 simple_border">
        <table class="w100 font_8 info_table">
            <tr>
                <td>
                    <p class="font_12"><b>${_("AMOUNT UNTAXED")}</b></p>
                    <p class="data font_12">${formatLang(inv.amount_untaxed or 0.00, digits=2)} ${inv.currency_id and inv.currency_id.symbol}</p>
                </td>
                <td>
                    <p class="font_12"><b>${_("AMOUNT TAX")}</b></p>
                    <p class="data font_12">${formatLang(inv.amount_tax or 0.00, digits=2)} ${inv.currency_id and inv.currency_id.symbol}</p>
                </td>
                <td>
                    <p class="font_12"><b>${_("TOTAL")}</b></p>
                    <p class="data font_12">${formatLang(inv.amount_total or 0.00, digits=2)} ${inv.currency_id and inv.currency_id.symbol}</p>
                </td>
                <td>
                    <p class="font_12"><b>${_("TO PAY")}</b></p>
                    <p class="data font_12">${formatLang(inv.residual or 0.00, digits=2)} ${inv.currency_id and inv.currency_id.symbol}</p>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <p>${_("DUE")}</p>
                    %if inv.move_id:
                        <table class="w100 font_9" style="margin-top:-5px;">
                        %for scadenza in inv.move_id.line_id:
                            %if scadenza.debit:
                                <tr>
                                    <td><p class="data">${scadenza.date_maturity or ''}</p></td>
                                    <td><p class="data">${formatLang(scadenza.debit or 0.00, digits=2)} &nbsp; ${inv.currency_id and inv.currency_id.symbol}</p></td>
                                </tr>
                            %endif
                        %endfor
                        </table>
                    %endif
                </td>
                <td colspan="3">
                    <p>${_("SIGNATURE DRIVER")}</p>
                    <p class="data">&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p>${_("GOOD DESCRIPTION")}</p>
                    <p class="data">${inv.goods_description_id and inv.goods_description_id.name or '&nbsp;'}</p>
                </td>
                <td>
                    <p>${_("PACKAGES NUMBER")}</p>
                    <p class="data">${inv.packages_number or 0.00}</p>
                </td>
                <td>
                    <p>${_("CARRIAGE CONDITION")}</p>
                    <p class="data">${inv.carriage_condition_id and inv.carriage_condition_id.name or '&nbsp;'}</p>
                </td>
                <td colspan="2">
                    <p>${_("SIGNATURE RECIPIENT")}</p>
                    <p class="data">&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <p>${_("DATE TRANP. START")}</p>
                    <p class="data">${datetime.today().strftime('%d/%m/%Y %H:%M')}</p>
                </td>
                <td colspan="3">
                    <p>${_("SIGNATURE VECTOR")}</p>
                    <p class="data">&nbsp;</p>
                </td>
            </tr>
        </table>
    </div>
</%def>

<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body class="font_10" style="margin:0px;padding:0px;">
    
    <% row_limit = 28 %>
    
    %for inv in objects:
        %for copy_number in (1,2):

            <% pagina_attuale = 1 %>
        
            <%self:inv_header inv="${inv}" page_number="${page_number}" row_limit="${row_limit}" pagina_attuale="${pagina_attuale}"></%self:inv_header>
        
            <% counter = 0 %>
            %for line in inv.invoice_line :
                <% counter += 1 %>
                %if counter > row_limit:
                    <% counter = 0 %>
                    <!-- ========== FOOTER ========== -->
                    <%self:inv_footer inv="${inv}"></%self:inv_footer>
                    <!-- ========== FOOTER ========== -->
                    <div class="page-break">&nbsp;</div>
                    <% pagina_attuale += 1 %>
                    <div class="clear">&nbsp;</div>
                    <!-- ========== HEADER ========== -->
                    <%self:inv_header inv="${inv}" page_number="${page_number}" row_limit="${row_limit}" pagina_attuale="${pagina_attuale}"></%self:inv_header>
                    <!-- ========== HEADER ========== -->
                %endif
                <tr>
                    <td class="w50">${line.name or ''}</td>
                    <td class="w5"><p class="centered">${line.uos_id.name or ''}</p></td>
                    <td class="amount w5"><p class="centered">${line.quantity or ''}</p></td>
                    <td class="amount w10"><p class="centered">${formatLang(line.price_unit or 0.00, digits=get_digits(dp='Account'))} ${inv.currency_id and inv.currency_id.symbol}</p></td>
                    <td class="amount w10"><p class="centered">${formatLang(line.discount or 0.00, digits=2)}</p></td>
                    <td class="amount w10"><p class="centered">${formatLang(line.price_unit * line.quantity, digits=get_digits(dp='Account'))} ${inv.currency_id and inv.currency_id.symbol}</p></td>
                    <td class="amount w10"><p class="centered">${line.invoice_line_tax_id and line.invoice_line_tax_id[0].description or ''}</p></td>
                </tr>
            %endfor
            
            %if counter <= row_limit:
                %for line in range(row_limit-counter):
                    <tr><td colspan="7">&nbsp;</td></tr>
                %endfor
            %endif

            <%self:inv_footer inv="${inv}"></%self:inv_footer>

            <div class="page-break">&nbsp;</div>
            <% pagina_attuale = +1 %>
    
        %endfor
    %endfor
</body>
</html>
