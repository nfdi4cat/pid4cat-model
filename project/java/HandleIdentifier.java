package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  A handle identifier.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleIdentifier extends RelatedIdentifier {

  private String resolvingUrl;
  private String identifier;

}
