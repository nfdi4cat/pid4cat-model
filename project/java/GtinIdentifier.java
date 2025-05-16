package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  A Global Trade Item Number (GTIN) previously called European Article Number (EAN) often encoded as EAN13 barcode. The identifier is used to identify products. GTINs don't have a resolvable URL.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GtinIdentifier extends RelatedIdentifier {

  private String identifier;

}
