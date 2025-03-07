package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  A Global Trade Item Number (GTIN) previously called European Article Number (EAN) often encoded as EAN13 barcode. The identifier is used to identify products. GTINs don't have a resolvable URL.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GtinIdentifier extends RelatedIdentifier {

  private String identifier;

}
