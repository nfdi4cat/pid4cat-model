package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  A PURL (permanent uniform resource locator).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PurlIdentifier extends RelatedIdentifier {

  private String resolvingUrl;

}
