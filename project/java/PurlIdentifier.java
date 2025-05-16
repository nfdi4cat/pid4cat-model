package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  A PURL (permanent uniform resource locator).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PurlIdentifier extends RelatedIdentifier {

  private String resolvingUrl;

}
