package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  A handle identifier.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleIdentifier extends RelatedIdentifier {

  private String resolvingUrl;
  private String identifier;

}
